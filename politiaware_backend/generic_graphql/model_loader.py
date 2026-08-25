"""
Model loader & introspection utilities for generic_graphql.
Resolves model strings to Django model classes and inspects model metadata.
"""

from typing import Optional, Type, Dict, Any, List
from django.apps import apps
from django.db import models


def get_django_model(model_identifier: str, app_label: Optional[str] = None) -> Type[models.Model]:
    """
    Resolves a model identifier string to a Django Model class.
    Supports:
      - "app_label.ModelName"
      - "ModelName" with app_label argument
      - "ModelName" (scans all installed apps)
    """
    if not isinstance(model_identifier, str):
        if issubclass(model_identifier, models.Model):
            return model_identifier
        raise TypeError(f"Expected model identifier as string or Model class, got {type(model_identifier)}")

    if "." in model_identifier:
        app_label, model_name = model_identifier.split(".", 1)
        return apps.get_model(app_label, model_name)

    if app_label:
        return apps.get_model(app_label, model_identifier)

    # Scan installed apps
    matched_models = []
    for m in apps.get_models():
        if m.__name__.lower() == model_identifier.lower():
            matched_models.append(m)

    if not matched_models:
        raise LookupError(
            f"Django model '{model_identifier}' not found in any installed app. "
            f"Please check your GRAPHQL_CONF or specify 'app_label'."
        )

    if len(matched_models) > 1:
        app_labels = [m._meta.app_label for m in matched_models]
        raise LookupError(
            f"Ambiguous model name '{model_identifier}' found in multiple apps: {app_labels}. "
            f"Please specify 'app_label' or use 'app_label.{model_identifier}' in GRAPHQL_CONF."
        )

    return matched_models[0]


def get_model_fields(model_cls: Type[models.Model]) -> Dict[str, Any]:
    """
    Returns a dictionary of {field_name: Field} for all direct concrete fields on the model,
    including inherited fields, and strictly excluding reverse relations.
    """
    field_dict = {}
    for f in model_cls._meta.get_fields():
        if not hasattr(f, "name"):
            continue
        # Exclude auto_created reverse relationships (ManyToOneRel, ManyToManyRel, etc.)
        if getattr(f, "auto_created", False) and f.is_relation:
            continue
        if f.is_relation and f.one_to_many:
            continue
        field_dict[f.name] = f
    return field_dict


def get_editable_fields(model_cls: Type[models.Model]) -> List[str]:
    """
    Returns a list of field names that are editable for create/update mutations.
    Excludes primary key auto fields and non-editable fields.
    """
    editable = []
    for f in model_cls._meta.get_fields():
        if not hasattr(f, "name"):
            continue
        if f.is_relation and f.one_to_many:
            continue
        if isinstance(f, (models.AutoField, models.BigAutoField, models.SmallAutoField)):
            continue
        if getattr(f, "editable", True):
            editable.append(f.name)
    return editable


def get_field_by_name(model_cls: Type[models.Model], field_name: str) -> Optional[Any]:
    """
    Gets a field by name, supporting direct fields or traversed relationship paths (e.g. 'party__abbreviation').
    """
    try:
        if "__" in field_name:
            parts = field_name.split("__")
            curr_model = model_cls
            curr_field = None
            for part in parts:
                curr_field = curr_model._meta.get_field(part)
                if curr_field.is_relation and hasattr(curr_field, "related_model") and curr_field.related_model:
                    curr_model = curr_field.related_model
            return curr_field
        return model_cls._meta.get_field(field_name)
    except Exception:
        return None
