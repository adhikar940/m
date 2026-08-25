"""
Structured / Nested Filter Input Object Types for generic_graphql.
Generates top-down operator dropdowns in GraphiQL (e.g. field -> exact, icontains, startswith, in).
"""

from typing import Any, Dict, List, Optional, Type
import graphene
from django.db import models

from .model_loader import get_field_by_name

# Standard Operator Filter Input Types
class StringFilterInput(graphene.InputObjectType):
    """Filter operators for text fields."""
    exact = graphene.String(description="Exact case-sensitive match")
    iexact = graphene.String(description="Exact case-insensitive match")
    contains = graphene.String(description="Contains substring (case-sensitive)")
    icontains = graphene.String(description="Contains substring (case-insensitive)")
    startswith = graphene.String(description="Starts with (case-sensitive)")
    istartswith = graphene.String(description="Starts with (case-insensitive)")
    endswith = graphene.String(description="Ends with (case-sensitive)")
    iendswith = graphene.String(description="Ends with (case-insensitive)")
    in_list = graphene.List(graphene.String, name="in", description="Matches any string in the list")
    regex = graphene.String(description="Matches regular expression")
    iregex = graphene.String(description="Matches regular expression (case-insensitive)")
    isnull = graphene.Boolean(description="Check if value is null")


class IntFilterInput(graphene.InputObjectType):
    """Filter operators for integer numeric fields."""
    exact = graphene.Int(description="Exact integer match")
    gt = graphene.Int(description="Greater than (>)")
    gte = graphene.Int(description="Greater than or equal to (>=)")
    lt = graphene.Int(description="Less than (<)")
    lte = graphene.Int(description="Less than or equal to (<=)")
    in_list = graphene.List(graphene.Int, name="in", description="Matches any integer in the list")
    range = graphene.List(graphene.Int, description="Between two integers [min, max]")
    isnull = graphene.Boolean(description="Check if value is null")


class IdFilterInput(graphene.InputObjectType):
    """Filter operators for ID and Foreign Key fields."""
    exact = graphene.ID(description="Exact ID match")
    in_list = graphene.List(graphene.ID, name="in", description="Matches any ID in the list")
    gt = graphene.ID(description="Greater than ID")
    gte = graphene.ID(description="Greater than or equal ID")
    lt = graphene.ID(description="Less than ID")
    lte = graphene.ID(description="Less than or equal ID")
    isnull = graphene.Boolean(description="Check if relation is null")


class FloatFilterInput(graphene.InputObjectType):
    """Filter operators for float/decimal numeric fields."""
    exact = graphene.Float(description="Exact float match")
    gt = graphene.Float(description="Greater than (>)")
    gte = graphene.Float(description="Greater than or equal to (>=)")
    lt = graphene.Float(description="Less than (<)")
    lte = graphene.Float(description="Less than or equal to (<=)")
    range = graphene.List(graphene.Float, description="Between two floats [min, max]")
    isnull = graphene.Boolean(description="Check if value is null")


class DateFilterInput(graphene.InputObjectType):
    """Filter operators for Date fields."""
    exact = graphene.Date(description="Exact date match (YYYY-MM-DD)")
    gt = graphene.Date(description="After date (>)")
    gte = graphene.Date(description="On or after date (>=)")
    lt = graphene.Date(description="Before date (<)")
    lte = graphene.Date(description="On or before date (<=)")
    range = graphene.List(graphene.Date, description="Between two dates [start, end]")
    year = graphene.Int(description="Matches year (YYYY)")
    month = graphene.Int(description="Matches month (1-12)")
    day = graphene.Int(description="Matches day of month (1-31)")
    isnull = graphene.Boolean(description="Check if date is null")


class DateTimeFilterInput(graphene.InputObjectType):
    """Filter operators for DateTime fields."""
    exact = graphene.DateTime(description="Exact datetime match")
    gt = graphene.DateTime(description="After datetime (>)")
    gte = graphene.DateTime(description="On or after datetime (>=)")
    lt = graphene.DateTime(description="Before datetime (<)")
    lte = graphene.DateTime(description="On or before datetime (<=)")
    range = graphene.List(graphene.DateTime, description="Between two datetimes [start, end]")
    date = graphene.Date(description="Matches date portion")
    year = graphene.Int(description="Matches year (YYYY)")
    month = graphene.Int(description="Matches month (1-12)")
    day = graphene.Int(description="Matches day of month (1-31)")
    isnull = graphene.Boolean(description="Check if datetime is null")


class BooleanFilterInput(graphene.InputObjectType):
    """Filter operators for boolean fields."""
    exact = graphene.Boolean(description="Exact boolean match (true/false)")
    isnull = graphene.Boolean(description="Check if boolean is null")


_MODEL_FILTER_REGISTRY: Dict[str, Type[graphene.InputObjectType]] = {}


def get_filter_input_for_django_field(django_field: Optional[models.Field]) -> Type[graphene.InputObjectType]:
    """Returns the appropriate filter operator input type for a Django model field."""
    if django_field is None:
        return StringFilterInput

    if isinstance(django_field, (models.AutoField, models.BigAutoField, models.SmallAutoField,
                                models.ForeignKey, models.OneToOneField)):
        return IdFilterInput

    if isinstance(django_field, (models.IntegerField, models.SmallIntegerField, models.BigIntegerField,
                                models.PositiveIntegerField, models.PositiveSmallIntegerField)):
        return IntFilterInput

    if isinstance(django_field, (models.FloatField, models.DecimalField)):
        return FloatFilterInput

    if isinstance(django_field, models.BooleanField):
        return BooleanFilterInput

    if isinstance(django_field, models.DateTimeField):
        return DateTimeFilterInput

    if isinstance(django_field, models.DateField):
        return DateFilterInput

    return StringFilterInput


def get_or_create_model_filter_type(
    model_cls: Type[models.Model],
    filter_fields: Dict[str, List[str]],
    type_name: Optional[str] = None
) -> Type[graphene.InputObjectType]:
    """
    Creates a top-down structured Filter Input Object for a model.
    E.g. PartyFilterInput with fields (id, partyname, abbreviation, foundeddate, ...)
    Each field expands to its supported operators (exact, icontains, in, etc.).
    """
    name = type_name or f"Generic_{model_cls._meta.app_label}_{model_cls.__name__}FilterInput"

    cache_key = f"{name}_{hash(tuple(sorted(filter_fields.keys())))}"
    if cache_key in _MODEL_FILTER_REGISTRY:
        return _MODEL_FILTER_REGISTRY[cache_key]

    attrs = {}
    for field_name in filter_fields.keys():
        field_obj = get_field_by_name(model_cls, field_name)
        filter_input_type = get_filter_input_for_django_field(field_obj)
        # Sanitized attribute name for GraphQL input
        safe_attr_name = field_name.replace("__", "_")
        attrs[safe_attr_name] = filter_input_type(
            description=f"Filter operators for {field_name}"
        )

    dynamic_filter_type = type(name, (graphene.InputObjectType,), attrs)
    _MODEL_FILTER_REGISTRY[cache_key] = dynamic_filter_type
    return dynamic_filter_type


def parse_nested_filters(
    filters_data: Dict[str, Any],
    field_name_map: Optional[Dict[str, str]] = None
) -> Dict[str, Any]:
    """
    Parses a nested filter dictionary from GraphQL into Django ORM lookup expressions.
    Example:
      filters_data = {
         "abbreviation": {"icontains": "BJP", "in": ["BJP", "INC"]},
         "foundeddate": {"gte": "2000-01-01"}
      }
      Returns:
      {
         "abbreviation__icontains": "BJP",
         "abbreviation__in": ["BJP", "INC"],
         "foundeddate__gte": "2000-01-01"
      }
    """
    orm_filters = {}
    field_name_map = field_name_map or {}

    for field_attr, ops in filters_data.items():
        if not ops or not isinstance(ops, dict):
            continue

        # Restore original ORM field name (e.g. party_abbreviation -> party__abbreviation)
        orm_field = field_name_map.get(field_attr, field_attr)

        for op_name, op_val in ops.items():
            if op_val is None:
                continue

            # In Graphene, 'in' is mapped to 'in_list' or 'in'
            if op_name in ("in_list", "in"):
                orm_expr = f"{orm_field}__in"
            elif op_name == "exact":
                orm_expr = orm_field
            else:
                orm_expr = f"{orm_field}__{op_name}"

            orm_filters[orm_expr] = op_val

    return orm_filters
