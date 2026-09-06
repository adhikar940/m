"""
Dynamic Query Generator for generic_graphql.
Builds get, list (with top-down structured filters, pagination, search, sorting), and extra queries.
"""

from typing import Any, Dict, List, Optional, Tuple, Type
import graphene
from django.db import models
from django.db.models import Q

from .type_factory import (
    get_or_create_django_type,
    get_or_create_paginated_type,
    PaginatedResult,
    extract_selected_model_fields
)
from .filter_factory import get_or_create_model_filter_type, parse_nested_filters


def _format_query_name(model_name: str, prefix: str = "", suffix: str = "") -> str:
    """Formats a model name into a camelCase GraphQL query name (e.g. allLokSabhaMPs, allPartys, allDistricts)."""
    clean_name = model_name[0].upper() + model_name[1:] if model_name else ""
    if suffix.lower() == "s" and clean_name.lower().endswith("s"):
        suffix = ""
    if prefix:
        return f"{prefix}{clean_name}{suffix}"
    return f"{model_name[0].lower()}{model_name[1:]}{suffix}"


def wrap_custom_list_resolver(custom_resolver: Any):
    """Wraps a custom resolver ensuring paginated response format."""
    def wrapped(self, info, **kwargs):
        res = custom_resolver(self, info, **kwargs)
        if isinstance(res, (dict, PaginatedResult)):
            return res
        if hasattr(res, "__iter__") or hasattr(res, "count"):
            offset = kwargs.get("offset")
            if offset is None:
                offset = 0
            limit = kwargs.get("limit")
            if limit is None:
                limit = 10
            model_cls = getattr(res, "model", None)
            if hasattr(res, "only") and model_cls:
                return PaginatedResult(qs=res, offset=offset, limit=limit, model_cls=model_cls)
            paged = res[offset:offset + limit]
            return {
                "total": res.count() if hasattr(res, "count") else len(res),
                "offset": offset,
                "limit": limit,
                "data": paged,
            }
        return res
    return wrapped


def create_generic_list_resolver(
    model_cls: Type[models.Model],
    field_name_map: Dict[str, str],
    search_fields: List[str],
    custom_queryset_hook: Optional[Any] = None
):
    """
    Creates a resolver function for the generic list query supporting top-down nested filters,
    search, ordering, and lazy pagination metadata (total, offset, limit, data).
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

        # 4. Pagination Arguments (default limit=10, default offset=0)
        offset = kwargs.get("offset")
        if offset is None:
            offset = 0

        limit = kwargs.get("limit")
        if limit is None:
            limit = 10

        # Return lazy PaginatedResult (database queries executed on-demand with .only() and lazy count)
        return PaginatedResult(qs=qs, offset=offset, limit=limit, model_cls=model_cls)

    return resolver


def build_model_queries(
    model_name: str,
    normalized_config: Dict[str, Any]
) -> Dict[str, Tuple[graphene.Field, Any]]:
    """
    Builds all query fields and resolvers for a single model (get, list, extra).
    Returns: { field_name: (graphene_field_definition, resolver_function) }
    """
    queries_dict = {}
    model_cls = normalized_config["model_cls"]
    queries_cfg = normalized_config.get("queries") or {}

    # 1. List Query (with Top-Down Structured Filters, Search, Ordering, and Pagination Metadata)
    list_cfg = queries_cfg.get("list")
    if list_cfg and list_cfg.get("enabled", True):
        return_cols = list_cfg.get("return_cols", "__all__")
        custom_type = list_cfg.get("type")
        django_type = custom_type if custom_type else get_or_create_django_type(model_cls, return_cols=return_cols)
        paginated_type = get_or_create_paginated_type(model_cls, django_type)

        query_name = list_cfg.get("name") or _format_query_name(model_cls.__name__, prefix="all", suffix="s")

        # Build Top-Down Filter Input Object Type
        filter_fields = list_cfg.get("filter_fields") or {}
        filter_depth = list_cfg.get("filter_depth", 3)
        filter_type = get_or_create_model_filter_type(model_cls, filter_fields, max_depth=filter_depth)

        # Mapping for nested field names (e.g. party_abbreviation -> party__abbreviation)
        field_name_map = {fname.replace("__", "_"): fname for fname in filter_fields.keys()}

        list_args = {
            "filters": filter_type(description=f"Top-down filters for {model_cls.__name__} fields and operators"),
        }

        # Pagination arguments
        if list_cfg.get("pagination", True):
            list_args["limit"] = graphene.Int(default_value=10, description="Number of items to return (default: 10)")
            list_args["offset"] = graphene.Int(default_value=0, description="Number of items to skip (default: 0)")

        # Text search argument
        search_fields = list_cfg.get("search_fields") or []
        if search_fields:
            list_args["search"] = graphene.String(description=f"Search across {', '.join(search_fields)}")

        # Ordering arguments (supports single string or list of columns, e.g. ['-id', 'name'] or '-id')
        list_args["order_by"] = graphene.List(graphene.String, description="Ordering fields (e.g. ['-id', 'name'])")

        list_field = graphene.Field(
            paginated_type,
            **list_args,
            description=f"List, filter, and paginate {model_cls.__name__} records"
        )

        custom_res = list_cfg.get("resolver")
        get_qs_hook = list_cfg.get("get_queryset")
        resolver_fn = wrap_custom_list_resolver(custom_res) if custom_res else create_generic_list_resolver(
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
