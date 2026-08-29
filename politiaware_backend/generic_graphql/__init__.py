"""
generic_graphql: Automated, config-driven GraphQL query & mutation generator for Django & Graphene.
"""

from .builder import generate_generic_graphql
from .type_factory import (
    get_or_create_django_type,
    get_or_create_payload_type,
    get_or_create_paginated_type,
    PaginatedResult,
    extract_selected_model_fields,
    DeletePayload
)
from .model_loader import get_django_model, get_model_fields, get_editable_fields
from .filter_factory import (
    StringFilterInput,
    IntFilterInput,
    IdFilterInput,
    FloatFilterInput,
    DateFilterInput,
    DateTimeFilterInput,
    BooleanFilterInput,
    get_or_create_model_filter_type,
    parse_nested_filters
)

__all__ = [
    "generate_generic_graphql",
    "get_or_create_django_type",
    "get_or_create_payload_type",
    "get_or_create_paginated_type",
    "PaginatedResult",
    "extract_selected_model_fields",
    "DeletePayload",
    "get_django_model",
    "get_model_fields",
    "get_editable_fields",
    "StringFilterInput",
    "IntFilterInput",
    "IdFilterInput",
    "FloatFilterInput",
    "DateFilterInput",
    "DateTimeFilterInput",
    "BooleanFilterInput",
    "get_or_create_model_filter_type",
    "parse_nested_filters",
]
