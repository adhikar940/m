"""
Schema Builder orchestrator for generic_graphql.
Iterates over GRAPHQL_CONF, generates all queries & mutations, and returns GenericQuery & GenericMutation.
"""

from typing import Any, Dict, List, Optional, Tuple, Type
import graphene

from .model_loader import get_django_model
from .config_parser import normalize_model_config, resolve_callable
from .query_factory import build_model_queries
from .mutation_factory import build_model_mutations


def generate_generic_graphql(
    graphql_conf: Dict[str, Any]
) -> Tuple[Type[graphene.ObjectType], Type[graphene.ObjectType]]:
    """
    Main entry point for generic_graphql.
    Parses GRAPHQL_CONF and dynamically creates GenericQuery and GenericMutation classes.

    Usage:
        GenericQuery, GenericMutation = generate_generic_graphql(GRAPHQL_CONF)
    """
    query_attrs: Dict[str, Any] = {}
    mutation_attrs: Dict[str, Any] = {}

    extra_query_classes: List[Type[graphene.ObjectType]] = []
    extra_mutation_classes: List[Type[graphene.ObjectType]] = []

    for key, val in graphql_conf.items():
        # Handle global extra queries / mutations
        if key == "__extra_queries__":
            if isinstance(val, (list, tuple)):
                for q_item in val:
                    resolved = resolve_callable(q_item)
                    if resolved and isinstance(resolved, type) and issubclass(resolved, graphene.ObjectType):
                        extra_query_classes.append(resolved)
            continue

        if key == "__extra_mutations__":
            if isinstance(val, (list, tuple)):
                for m_item in val:
                    resolved = resolve_callable(m_item)
                    if resolved and isinstance(resolved, type) and issubclass(resolved, graphene.ObjectType):
                        extra_mutation_classes.append(resolved)
            continue

        # Process Model configuration
        model_name = key
        raw_config = val or {}

        try:
            model_cls = get_django_model(
                model_identifier=model_name,
                app_label=raw_config.get("app_label") if isinstance(raw_config, dict) else None
            )
        except Exception as exc:
            # Skip invalid or non-model keys with a clear warning or raise
            raise LookupError(f"Could not load model for config key '{model_name}': {exc}") from exc

        normalized_config = normalize_model_config(
            model_identifier=model_name,
            raw_config=raw_config,
            model_cls=model_cls
        )

        # 1. Build Queries
        model_queries = build_model_queries(model_name, normalized_config)
        for q_name, (field_def, resolver_fn) in model_queries.items():
            query_attrs[q_name] = field_def
            if resolver_fn:
                resolver_name = f"resolve_{q_name}"
                query_attrs[resolver_name] = resolver_fn

        # 2. Build Mutations
        model_mutations = build_model_mutations(model_name, normalized_config)
        for m_name, mut_field in model_mutations.items():
            mutation_attrs[m_name] = mut_field

    # Dynamically build GenericQuery ObjectType
    query_bases = tuple(extra_query_classes) + (graphene.ObjectType,)
    GenericQuery = type("GenericQuery", query_bases, query_attrs)

    # Dynamically build GenericMutation ObjectType
    mutation_bases = tuple(extra_mutation_classes) + (graphene.ObjectType,)
    GenericMutation = type("GenericMutation", mutation_bases, mutation_attrs)

    return GenericQuery, GenericMutation
