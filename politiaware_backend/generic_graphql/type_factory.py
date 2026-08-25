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
      - <model_name_lower> (alias to data)
    """
    name = payload_name or f"Generic_{model_cls._meta.app_label}_{model_cls.__name__}Payload"
    if name in _PAYLOAD_TYPE_REGISTRY:
        return _PAYLOAD_TYPE_REGISTRY[name]

    model_field_name = model_cls.__name__.lower()

    def resolve_model_alias(self, info):
        return getattr(self, "data", None)

    attrs = {
        "success": graphene.Boolean(required=True),
        "errors": graphene.List(graphene.String),
        "data": graphene.Field(data_type),
        # Model-name alias e.g. "party" or "loksabhaconstituency"
        model_field_name: graphene.Field(data_type, resolver=resolve_model_alias)
    }

    dynamic_payload = type(name, (graphene.ObjectType,), attrs)
    _PAYLOAD_TYPE_REGISTRY[name] = dynamic_payload
    return dynamic_payload
