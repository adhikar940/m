"""
Dynamic Query Generator for generic_graphql.
Builds get, list (with top-down structured filters, pagination, search, sorting), and extra queries.
"""

from typing import Any, Dict, List, Optional, Tuple, Type
import graphene
from django.db import models
from django.db.models import Q

from .model_loader import get_field_by_name
from .field_mapper import django_field_to_graphene_type
from .type_factory import get_or_create_django_type
from .filter_factory import get_or_create_model_filter_type, parse_nested_filters


def _format_query_name(model_name: str, prefix: str = "", suffix: str = "") -> str:
    """Formats a model name into a camelCase GraphQL query name (e.g. allLokSabhaMPs, lokSabhaMP, party, allPartys)."""
    clean_name = model_name[0].upper() + model_name[1:] if model_name else ""
    if prefix:
        return f"{prefix}{clean_name}{suffix}"
    return f"{model_name[0].lower()}{model_name[1:]}{suffix}"


def create_generic_list_resolver(
    model_cls: Type[models.Model],
    field_name_map: Dict[str, str],
    search_fields: List[str],
    custom_queryset_hook: Optional[Any] = None
):
    """
    Creates a resolver function for the generic list query supporting top-down nested filters.
    """
    def resolver(self, info, **kwargs):
        qs = model_cls.objects.all()

        # Apply custom get_queryset hook if defined
        if custom_queryset_hook:
            qs = custom_queryset_hook(qs, info, **kwargs)

        # 1. Apply Top-Down Structured Filters
        filters_data = kwargs.get("filters")
        if filters_data and isinstance(filters_data, dict):
            orm_filters = parse_nested_filters(filters_data, field_name_map)
            if orm_filters:
                qs = qs.filter(**orm_filters)

        # 2. Apply Text Search
        search_term = kwargs.get("search")
        if search_term and search_fields:
            search_query = Q()
            for sf in search_fields:
                search_query |= Q(**{f"{sf}__icontains": search_term})
            qs = qs.filter(search_query)

        # 3. Apply Ordering
        order_by = kwargs.get("order_by") or kwargs.get("orderBy")
        if order_by:
            if isinstance(order_by, str):
                order_by = [order_by]
            qs = qs.order_by(*order_by)

        # 4. Apply Pagination
        offset = kwargs.get("offset")
        limit = kwargs.get("limit")

        if offset is not None:
            qs = qs[offset:]
        if limit is not None:
            qs = qs[:limit]

        return qs

    return resolver


def create_generic_get_resolver(
    model_cls: Type[models.Model],
    pk_field_name: str = "id"
):
    """
    Creates a resolver function for fetching a single model instance by PK.
    """
    def resolver(self, info, **kwargs):
        pk_val = kwargs.get(pk_field_name) or kwargs.get("id")
        if pk_val is None:
            return None
        try:
            return model_cls.objects.filter(**{pk_field_name: pk_val}).first()
        except Exception:
            return None

    return resolver


def build_model_queries(
    model_name: str,
    normalized_config: Dict[str, Any]
) -> Dict[str, Tuple[graphene.Field, Any]]:
    """
    Builds all query fields and resolvers for a single model.
    Returns: { field_name: (graphene_field_definition, resolver_function) }
    """
    queries_dict = {}
    model_cls = normalized_config["model_cls"]
    queries_cfg = normalized_config.get("queries") or {}

    # 1. Single Item (Get) Query
    get_cfg = queries_cfg.get("get")
    if get_cfg and get_cfg.get("enabled", True):
        pk_field_name = get_cfg.get("pk", "id")
        return_cols = get_cfg.get("return_cols", "__all__")
        django_type = get_or_create_django_type(model_cls, return_cols=return_cols)

        query_name = get_cfg.get("name") or _format_query_name(model_cls.__name__)
        pk_field = get_field_by_name(model_cls, pk_field_name)
        pk_graphene_type = django_field_to_graphene_type(pk_field)

        get_field = graphene.Field(
            django_type,
            **{pk_field_name: pk_graphene_type(required=True)},
            description=f"Fetch a single {model_cls.__name__} by {pk_field_name}"
        )

        custom_res = get_cfg.get("resolver")
        resolver_fn = custom_res if custom_res else create_generic_get_resolver(model_cls, pk_field_name)
        queries_dict[query_name] = (get_field, resolver_fn)

    # 2. List Query (with Top-Down Structured Filters, Search, Ordering, Pagination)
    list_cfg = queries_cfg.get("list")
    if list_cfg and list_cfg.get("enabled", True):
        return_cols = list_cfg.get("return_cols", "__all__")
        custom_type = list_cfg.get("type")
        django_type = custom_type if custom_type else get_or_create_django_type(model_cls, return_cols=return_cols)

        query_name = list_cfg.get("name") or _format_query_name(model_cls.__name__, prefix="all", suffix="s")

        # Build Top-Down Filter Input Object Type
        filter_fields = list_cfg.get("filter_fields") or {}
        filter_type = get_or_create_model_filter_type(model_cls, filter_fields)

        # Mapping for nested field names (e.g. party_abbreviation -> party__abbreviation)
        field_name_map = {fname.replace("__", "_"): fname for fname in filter_fields.keys()}

        list_args = {
            "filters": filter_type(description=f"Top-down filters for {model_cls.__name__} fields and operators"),
        }

        # Pagination arguments
        if list_cfg.get("pagination", True):
            list_args["limit"] = graphene.Int(description="Number of items to return")
            list_args["offset"] = graphene.Int(description="Number of items to skip")

        # Text search argument
        search_fields = list_cfg.get("search_fields") or []
        if search_fields:
            list_args["search"] = graphene.String(description=f"Search across {', '.join(search_fields)}")

        # Ordering arguments
        list_args["order_by"] = graphene.List(graphene.String, description="Ordering fields (e.g. ['-id', 'name'])")
        list_args["orderBy"] = graphene.String(description="Ordering field alias (e.g. '-id')")

        list_field = graphene.List(
            django_type,
            **list_args,
            description=f"List and filter {model_cls.__name__} records"
        )

        custom_res = list_cfg.get("resolver")
        get_qs_hook = list_cfg.get("get_queryset")
        resolver_fn = custom_res if custom_res else create_generic_list_resolver(
            model_cls, field_name_map, search_fields, get_qs_hook
        )
        queries_dict[query_name] = (list_field, resolver_fn)

    # 3. Model-level Extra Queries
    extra_cfg = queries_cfg.get("extra") or {}
    for extra_name, extra_val in extra_cfg.items():
        if isinstance(extra_val, dict):
            extra_type = extra_val.get("type") or graphene.String
            extra_args = extra_val.get("args") or {}
            extra_resolver = extra_val.get("resolver")

            if isinstance(extra_type, type) and issubclass(extra_type, graphene.ObjectType):
                field_def = graphene.Field(extra_type, **extra_args)
            elif isinstance(extra_type, graphene.Structure):
                field_def = extra_type
            else:
                field_def = graphene.Field(extra_type, **extra_args)

            queries_dict[extra_name] = (field_def, extra_resolver)
        elif hasattr(extra_val, "resolve"):
            queries_dict[extra_name] = (extra_val, extra_val.resolve)

    return queries_dict
