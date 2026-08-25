"""
Field type mappings between Django Model fields and Graphene scalar/filter types.
"""

from typing import Dict, List, Type, Any, Optional
import graphene
from graphene.types.generic import GenericScalar
from django.db import models

# Default lookup operations supported per Django model field type
DEFAULT_TYPE_LOOKUPS: Dict[Type[models.Field], List[str]] = {
    models.CharField: ["exact", "iexact", "icontains", "istartswith", "iendswith", "in"],
    models.SlugField: ["exact", "iexact", "icontains", "in"],
    models.URLField: ["exact", "icontains", "in"],
    models.TextField: ["exact", "icontains", "istartswith"],
    models.EmailField: ["exact", "iexact", "icontains", "in"],
    models.IntegerField: ["exact", "gt", "gte", "lt", "lte", "in", "range"],
    models.SmallIntegerField: ["exact", "gt", "gte", "lt", "lte", "in", "range"],
    models.BigIntegerField: ["exact", "gt", "gte", "lt", "lte", "in", "range"],
    models.PositiveIntegerField: ["exact", "gt", "gte", "lt", "lte", "in", "range"],
    models.PositiveSmallIntegerField: ["exact", "gt", "gte", "lt", "lte", "in", "range"],
    models.FloatField: ["exact", "gt", "gte", "lt", "lte", "range"],
    models.DecimalField: ["exact", "gt", "gte", "lt", "lte", "range"],
    models.DateField: ["exact", "gt", "gte", "lt", "lte", "range", "year", "month", "day", "isnull"],
    models.DateTimeField: ["exact", "gt", "gte", "lt", "lte", "range", "year", "month", "day", "date", "isnull"],
    models.TimeField: ["exact", "gt", "gte", "lt", "lte", "isnull"],
    models.BooleanField: ["exact", "isnull"],
    models.ForeignKey: ["exact", "in", "isnull"],
    models.OneToOneField: ["exact", "in", "isnull"],
    models.AutoField: ["exact", "in"],
    models.BigAutoField: ["exact", "in"],
    models.JSONField: ["exact", "has_key", "contains", "isnull"],
    models.FileField: ["exact", "isnull"],
    models.ImageField: ["exact", "isnull"],
}


def get_default_lookups_for_field(django_field: models.Field) -> List[str]:
    """Returns default lookups for a given Django model field."""
    for field_cls, lookups in DEFAULT_TYPE_LOOKUPS.items():
        if isinstance(django_field, field_cls):
            return lookups
    return ["exact", "isnull"]


def django_field_to_graphene_type(django_field: Optional[models.Field], is_input: bool = False) -> Any:
    """
    Maps a Django model field to its corresponding Graphene base type.
    """
    if django_field is None:
        return graphene.String

    if isinstance(django_field, (models.AutoField, models.BigAutoField, models.SmallAutoField)):
        return graphene.ID

    if isinstance(django_field, (models.ForeignKey, models.OneToOneField)):
        # In inputs or ID filters, FK is passed as ID
        return graphene.ID

    if isinstance(django_field, (models.IntegerField, models.SmallIntegerField, models.BigIntegerField,
                                models.PositiveIntegerField, models.PositiveSmallIntegerField)):
        return graphene.Int

    if isinstance(django_field, (models.FloatField, models.DecimalField)):
        return graphene.Float

    if isinstance(django_field, models.BooleanField):
        return graphene.Boolean

    if isinstance(django_field, models.DateField):
        return graphene.Date

    if isinstance(django_field, models.DateTimeField):
        return graphene.DateTime

    if isinstance(django_field, models.TimeField):
        return graphene.Time

    if isinstance(django_field, models.JSONField):
        return GenericScalar

    # For ImageField and FileField in input, we accept String (URL / filepath)
    if isinstance(django_field, (models.FileField, models.ImageField)):
        return graphene.String

    # CharField, TextField, EmailField, SlugField, etc.
    return graphene.String


def get_graphene_argument_for_lookup(base_graphene_type: Any, lookup: str, required: bool = False) -> Any:
    """
    Converts a base Graphene type + lookup into the correct argument type.
    E.g. lookup='in' -> graphene.List(base_graphene_type)
         lookup='isnull' -> graphene.Boolean()
         lookup='year' -> graphene.Int()
         lookup='range' -> graphene.List(base_graphene_type)
    """
    if lookup == "isnull":
        return graphene.Boolean(required=required)

    if lookup in ("in", "range"):
        return graphene.List(base_graphene_type, required=required)

    if lookup in ("year", "month", "day", "week", "week_day", "iso_week_day", "quarter", "hour", "minute", "second"):
        return graphene.Int(required=required)

    if lookup == "date":
        return graphene.Date(required=required)

    if lookup == "time":
        return graphene.Time(required=required)

    if lookup in ("has_key", "regex", "iregex"):
        return graphene.String(required=required)

    if lookup == "has_keys" or lookup == "has_any_keys":
        return graphene.List(graphene.String, required=required)

    return base_graphene_type(required=required)
