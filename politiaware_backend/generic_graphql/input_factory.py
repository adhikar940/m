"""
Dynamic Graphene InputObjectType factory for generic_graphql mutations.
"""

from typing import Dict, List, Optional, Type
import graphene
from django.db import models

from .model_loader import get_field_by_name
from .field_mapper import django_field_to_graphene_type

_INPUT_TYPE_REGISTRY: Dict[str, Type[graphene.InputObjectType]] = {}


def get_or_create_input_type(
    model_cls: Type[models.Model],
    field_names: List[str],
    is_update: bool = False,
    required_cols: Optional[List[str]] = None,
    type_name: Optional[str] = None
) -> Type[graphene.InputObjectType]:
    """
    Dynamically generates an InputObjectType for create/update mutations.
    """
    required_cols = required_cols or []
    action_prefix = "Update" if is_update else "Create"
    name = type_name or f"Generic_{model_cls._meta.app_label}_{action_prefix}_{model_cls.__name__}Input"

    cache_key = f"{name}_{hash(tuple(sorted(field_names)))}"
    if cache_key in _INPUT_TYPE_REGISTRY:
        return _INPUT_TYPE_REGISTRY[cache_key]

    attrs = {}
    for col in field_names:
        field_obj = get_field_by_name(model_cls, col)
        graphene_base = django_field_to_graphene_type(field_obj, is_input=True)

        is_req = False
        if not is_update and col in required_cols:
            is_req = True

        attrs[col] = graphene_base(required=is_req)

    dynamic_input = type(name, (graphene.InputObjectType,), attrs)
    _INPUT_TYPE_REGISTRY[cache_key] = dynamic_input
    return dynamic_input


def get_mutation_arguments_dict(
    model_cls: Type[models.Model],
    field_names: List[str],
    is_update: bool = False,
    required_cols: Optional[List[str]] = None,
    use_input_object: bool = True,
    pk_field_name: str = "id"
) -> Dict[str, Any]:
    """
    Returns arguments for a mutation class.
    If use_input_object=True: returns {"input": InputType(...)} + pk if update.
    Otherwise returns flat argument fields.
    """
    required_cols = required_cols or []
    args = {}

    if is_update:
        # Update always requires pk argument
        pk_field = get_field_by_name(model_cls, pk_field_name)
        pk_type = django_field_to_graphene_type(pk_field)
        args[pk_field_name] = pk_type(required=True)

    if use_input_object:
        input_type = get_or_create_input_type(
            model_cls=model_cls,
            field_names=field_names,
            is_update=is_update,
            required_cols=required_cols
        )
        args["input"] = input_type(required=True)
    else:
        for col in field_names:
            field_obj = get_field_by_name(model_cls, col)
            graphene_base = django_field_to_graphene_type(field_obj, is_input=True)
            is_req = not is_update and col in required_cols
            args[col] = graphene_base(required=is_req)

    return args
