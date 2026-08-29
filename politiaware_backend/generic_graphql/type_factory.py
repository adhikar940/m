"""
Dynamic Graphene ObjectType and Payload factory for generic_graphql.
"""

from typing import Any, Dict, List, Optional, Type, Union
import graphene
from graphene_django import DjangoObjectType
from django.db import models

# Registry cache for dynamically created GraphQL types to prevent duplicate registrations
_DJANGO_TYPE_REGISTRY: Dict[str, Type[DjangoObjectType]] = {}
_PAYLOAD_TYPE_REGISTRY: Dict[str, Type[graphene.ObjectType]] = {}
_PAGINATED_TYPE_REGISTRY: Dict[str, Type[graphene.ObjectType]] = {}


class DeletePayload(graphene.ObjectType):
    """Standardized payload for delete mutations."""
    success = graphene.Boolean(required=True)
    errors = graphene.List(graphene.String)
    id = graphene.ID()


def get_or_create_django_type(
    model_cls: Type[models.Model],
    return_cols: Union[str, List[str]] = "__all__",
    type_name: Optional[str] = None
) -> Type[DjangoObjectType]:
    """
    Creates and caches a dynamic DjangoObjectType for a given Django model.
    """
    base_name = type_name or f"Generic{model_cls.__name__}Type"

    # If specific return columns are requested, key by columns to allow tailored types
    cache_key = f"{base_name}_{hash(tuple(sorted(return_cols)) if isinstance(return_cols, list) else return_cols)}"

    if cache_key in _DJANGO_TYPE_REGISTRY:
        return _DJANGO_TYPE_REGISTRY[cache_key]

    if return_cols == "__all__":
        # Include all direct model fields, excluding reverse relations
        from .model_loader import get_model_fields
        fields = list(get_model_fields(model_cls).keys())
    else:
        fields = list(return_cols)
        # Ensure primary key is included for DjangoObjectType resolution
        pk_name = model_cls._meta.pk.name
        if pk_name not in fields and "id" not in fields:
            fields.append(pk_name)

    meta_dict = {
        "model": model_cls,
        "fields": fields,
    }
    Meta = type("Meta", (), meta_dict)

    # Use a unique class name so GraphQL schema doesn't conflict
    unique_class_name = f"Generic_{model_cls._meta.app_label}_{model_cls.__name__}Type"
    dynamic_type = type(unique_class_name, (DjangoObjectType,), {"Meta": Meta})

    _DJANGO_TYPE_REGISTRY[cache_key] = dynamic_type
    return dynamic_type


def get_or_create_payload_type(
    model_cls: Type[models.Model],
    data_type: Type[graphene.ObjectType],
    payload_name: Optional[str] = None
) -> Type[graphene.ObjectType]:
    """
    Creates a standardized mutation response payload containing:
      - success (Boolean)
      - errors ([String])
      - data (DjangoObjectType)
    """
    name = payload_name or f"Generic_{model_cls._meta.app_label}_{model_cls.__name__}Payload"
    if name in _PAYLOAD_TYPE_REGISTRY:
        return _PAYLOAD_TYPE_REGISTRY[name]

    attrs = {
        "success": graphene.Boolean(required=True),
        "errors": graphene.List(graphene.String),
        "data": graphene.Field(data_type),
    }

    dynamic_payload = type(name, (graphene.ObjectType,), attrs)
    _PAYLOAD_TYPE_REGISTRY[name] = dynamic_payload
    return dynamic_payload


def extract_selected_model_fields(info: Any, model_cls: Type[models.Model], subfield: Optional[str] = None) -> List[str]:
    """
    Extracts requested field names from GraphQL ResolveInfo AST and maps them to valid DB columns on model_cls.
    Always includes primary key for consistent Django model hydration.
    """
    if not info or not hasattr(info, "field_nodes") or not info.field_nodes:
        return []

    selected_raw: List[str] = []

    def collect_selections(selection_set):
        fields = []
        if not selection_set or not hasattr(selection_set, "selections"):
            return fields
        for sel in selection_set.selections:
            if hasattr(sel, "name") and hasattr(sel.name, "value"):
                field_name = sel.name.value
                if field_name != "__typename":
                    fields.append(field_name)
            elif hasattr(sel, "selection_set") and sel.selection_set:
                fields.extend(collect_selections(sel.selection_set))
        return fields

    for node in info.field_nodes:
        if not hasattr(node, "selection_set") or not node.selection_set:
            continue
        if subfield:
            for sel in node.selection_set.selections:
                if hasattr(sel, "name") and sel.name.value == subfield:
                    if hasattr(sel, "selection_set") and sel.selection_set:
                        selected_raw.extend(collect_selections(sel.selection_set))
        else:
            selected_raw.extend(collect_selections(node.selection_set))

    if not selected_raw:
        return []

    # Map requested GraphQL fields to concrete Django model columns
    valid_cols: List[str] = []
    field_map: Dict[str, str] = {}
    for f in model_cls._meta.concrete_fields:
        field_map[f.name.lower()] = f.name
        field_map[f.name.replace("_", "").lower()] = f.name
        if hasattr(f, "attname"):
            field_map[f.attname.lower()] = f.attname
            field_map[f.attname.replace("_", "").lower()] = f.attname

    for rf in selected_raw:
        key = rf.replace("_", "").lower()
        if key in field_map:
            matched = field_map[key]
            if matched not in valid_cols:
                valid_cols.append(matched)

    # Always ensure primary key is included in .only()
    pk_name = model_cls._meta.pk.name
    if pk_name not in valid_cols:
        valid_cols.append(pk_name)

    return valid_cols


class PaginatedResult:
    """
    Lazy container for paginated query results.
    Executes database queries strictly on-demand:
      - get_total(): executes `qs.count()` only if 'total' was requested.
      - get_data(info): executes `qs.only(...)` with limit/offset slicing only if 'data' was requested.
    """
    def __init__(
        self,
        qs: Any,
        offset: int = 0,
        limit: int = 10,
        model_cls: Optional[Type[models.Model]] = None
    ):
        self.qs = qs
        self.offset = offset
        self.limit = limit
        self.model_cls = model_cls

    def get_total(self) -> int:
        if hasattr(self.qs, "count"):
            return self.qs.count()
        return len(self.qs)

    def get_data(self, info: Any) -> Any:
        paged_qs = self.qs
        if self.model_cls and info and hasattr(paged_qs, "only"):
            selected_fields = extract_selected_model_fields(info, self.model_cls, subfield="data")
            if selected_fields:
                paged_qs = paged_qs.only(*selected_fields)
        return paged_qs[self.offset:self.offset + self.limit]


def get_or_create_paginated_type(
    model_cls: Type[models.Model],
    django_type: Type[DjangoObjectType],
    type_name: Optional[str] = None
) -> Type[graphene.ObjectType]:
    """
    Creates and caches a standardized paginated response type containing:
      - total (Int): Total count of matching records before pagination slicing (lazy evaluated)
      - offset (Int): The offset applied to the query
      - limit (Int): The limit applied to the query
      - data ([DjangoObjectType]): The list of items for the current page (lazy fetched with .only())
    """
    name = type_name or f"Generic_{model_cls._meta.app_label}_{model_cls.__name__}PaginatedType"
    if name in _PAGINATED_TYPE_REGISTRY:
        return _PAGINATED_TYPE_REGISTRY[name]

    def resolve_total_field(root, info):
        if hasattr(root, "get_total"):
            return root.get_total()
        if isinstance(root, dict):
            return root.get("total")
        return getattr(root, "total", None)

    def resolve_offset_field(root, info):
        if hasattr(root, "offset"):
            return root.offset
        if isinstance(root, dict):
            return root.get("offset", 0)
        return getattr(root, "offset", 0)

    def resolve_limit_field(root, info):
        if hasattr(root, "limit"):
            return root.limit
        if isinstance(root, dict):
            return root.get("limit", 10)
        return getattr(root, "limit", 10)

    def resolve_data_field(root, info):
        if hasattr(root, "get_data"):
            return root.get_data(info)
        if isinstance(root, dict):
            return root.get("data")
        return getattr(root, "data", None)

    attrs: Dict[str, Any] = {
        "total": graphene.Int(
            description=f"Total count of {model_cls.__name__} records matching query filters",
            resolver=resolve_total_field
        ),
        "offset": graphene.Int(
            description="Pagination offset applied",
            resolver=resolve_offset_field
        ),
        "limit": graphene.Int(
            description="Pagination limit applied",
            resolver=resolve_limit_field
        ),
        "data": graphene.List(
            django_type,
            description=f"List of {model_cls.__name__} records for current page",
            resolver=resolve_data_field
        ),
    }

    dynamic_paginated_type = type(name, (graphene.ObjectType,), attrs)
    _PAGINATED_TYPE_REGISTRY[name] = dynamic_paginated_type
    return dynamic_paginated_type
