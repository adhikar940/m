"""
Configuration normalization, smart defaults injection, and callable resolution for generic_graphql.
"""

import importlib
from typing import Any, Dict, Optional, Type
from django.db import models

from .model_loader import get_editable_fields, get_model_fields
from .field_mapper import get_default_lookups_for_field


def resolve_callable(func_or_path: Any) -> Any:
    """
    Resolves a callable or an import path string (e.g. 'app.module.func').
    Returns the resolved callable or None.
    """
    if func_or_path is None:
        return None
    if callable(func_or_path):
        return func_or_path
    if isinstance(func_or_path, str):
        if "." in func_or_path:
            mod_name, attr_name = func_or_path.rsplit(".", 1)
            try:
                mod = importlib.import_module(mod_name)
                return getattr(mod, attr_name)
            except (ImportError, AttributeError) as exc:
                raise ImportError(f"Could not resolve callable from path '{func_or_path}': {exc}") from exc
        raise ValueError(f"Invalid callable path format: '{func_or_path}'. Expected 'module.callable_name'.")
    return func_or_path


def build_default_queries_config(model_cls: Type[models.Model]) -> Dict[str, Any]:
    """Generates default queries configuration for a model."""
    model_fields = get_model_fields(model_cls)
    filter_fields = {}
    search_fields = []

    for fname, fobj in model_fields.items():
        filter_fields[fname] = get_default_lookups_for_field(fobj)
        if isinstance(fobj, (models.CharField, models.TextField)):
            search_fields.append(fname)

    return {
        "list": {
            "enabled": True,
            "return_cols": "__all__",
            "filter_fields": filter_fields,
            "search_fields": search_fields,
            "ordering_fields": "__all__",
            "pagination": True
        },
        "extra": {}
    }


def build_default_mutations_config(model_cls: Type[models.Model]) -> Dict[str, Any]:
    """Generates default mutations configuration for a model."""
    editable_cols = get_editable_fields(model_cls)
    return {
        "create": {
            "enabled": True,
            "create_cols": editable_cols,
            "return_cols": "__all__"
        },
        "update": {
            "enabled": True,
            "pk": "id",
            "update_cols": editable_cols,
            "return_cols": "__all__"
        },
        "delete": {
            "enabled": True,
            "pk": "id",
            "return_cols": ["id"]
        },
        "extra": {}
    }


def normalize_model_config(
    model_identifier: str,
    raw_config: Optional[Dict[str, Any]],
    model_cls: Type[models.Model]
) -> Dict[str, Any]:
    """
    Normalizes model configuration.
    If raw_config is empty or None: injects smart defaults (list + CRUD mutations).
    If raw_config is specified: strictly applies whitelist and configures only specified operations.
    """
    raw_config = raw_config or {}

    # Case 1: Zero configuration provided -> Full automated defaults
    has_queries_section = "queries" in raw_config
    has_mutations_section = "mutations" in raw_config

    if not has_queries_section and not has_mutations_section:
        # Empty config e.g. "LokSabhaMP": {} -> Generate list query + CRUD mutations
        return {
            "app_label": raw_config.get("app_label", model_cls._meta.app_label),
            "model_cls": model_cls,
            "queries": build_default_queries_config(model_cls),
            "mutations": build_default_mutations_config(model_cls)
        }

    # Case 2: Explicit configuration -> Whitelist approach
    normalized = {
        "app_label": raw_config.get("app_label", model_cls._meta.app_label),
        "model_cls": model_cls,
        "queries": {},
        "mutations": {}
    }

    # Process Queries
    if has_queries_section:
        queries_cfg = raw_config.get("queries") or {}
        default_queries = build_default_queries_config(model_cls)

        if "list" in queries_cfg:
            list_cfg = queries_cfg["list"] or {}
            # If filter_fields not specified, use auto default filters
            filter_fields = list_cfg.get("filter_fields")
            if filter_fields is None:
                filter_fields = default_queries["list"]["filter_fields"]

            search_fields = list_cfg.get("search_fields")
            if search_fields is None:
                search_fields = default_queries["list"]["search_fields"]

            normalized["queries"]["list"] = {
                "enabled": list_cfg.get("enabled", True),
                "name": list_cfg.get("name"),
                "return_cols": list_cfg.get("return_cols", "__all__"),
                "filter_fields": filter_fields,
                "search_fields": search_fields,
                "ordering_fields": list_cfg.get("ordering_fields", "__all__"),
                "pagination": list_cfg.get("pagination", True),
                "resolver": resolve_callable(list_cfg.get("resolver")),
                "get_queryset": resolve_callable(list_cfg.get("get_queryset")),
                "type": list_cfg.get("type")
            }

        # Extra queries for this model
        if "extra" in queries_cfg:
            normalized["queries"]["extra"] = {}
            for qname, qval in queries_cfg["extra"].items():
                if isinstance(qval, dict):
                    normalized["queries"]["extra"][qname] = {
                        "type": resolve_callable(qval.get("type")),
                        "args": qval.get("args", {}),
                        "resolver": resolve_callable(qval.get("resolver"))
                    }
                else:
                    normalized["queries"]["extra"][qname] = resolve_callable(qval)

    # Process Mutations
    if has_mutations_section:
        mutations_cfg = raw_config.get("mutations") or {}
        editable_cols = get_editable_fields(model_cls)

        if "create" in mutations_cfg:
            create_cfg = mutations_cfg["create"] or {}
            create_cols = create_cfg.get("create_cols", editable_cols)
            normalized["mutations"]["create"] = {
                "enabled": create_cfg.get("enabled", True),
                "name": create_cfg.get("name"),
                "create_cols": create_cols,
                "return_cols": create_cfg.get("return_cols", "__all__"),
                "required_cols": create_cfg.get("required_cols", []),
                "before_save": resolve_callable(create_cfg.get("before_save")),
                "after_save": resolve_callable(create_cfg.get("after_save")),
                "mutate": resolve_callable(create_cfg.get("mutate")),
            }

        if "update" in mutations_cfg:
            update_cfg = mutations_cfg["update"] or {}
            update_cols = update_cfg.get("update_cols") or update_cfg.get("create_cols", editable_cols)
            normalized["mutations"]["update"] = {
                "enabled": update_cfg.get("enabled", True),
                "name": update_cfg.get("name"),
                "pk": update_cfg.get("pk", "id"),
                "update_cols": update_cols,
                "return_cols": update_cfg.get("return_cols", "__all__"),
                "before_save": resolve_callable(update_cfg.get("before_save")),
                "after_save": resolve_callable(update_cfg.get("after_save")),
                "mutate": resolve_callable(update_cfg.get("mutate")),
            }

        if "delete" in mutations_cfg:
            delete_cfg = mutations_cfg["delete"] or {}
            normalized["mutations"]["delete"] = {
                "enabled": delete_cfg.get("enabled", True),
                "name": delete_cfg.get("name"),
                "pk": delete_cfg.get("pk", "id"),
                "return_cols": delete_cfg.get("return_cols", ["id"]),
                "before_delete": resolve_callable(delete_cfg.get("before_delete")),
                "after_delete": resolve_callable(delete_cfg.get("after_delete")),
                "mutate": resolve_callable(delete_cfg.get("mutate")),
            }

        # Extra mutations for this model
        if "extra" in mutations_cfg:
            normalized["mutations"]["extra"] = {}
            for mname, mval in mutations_cfg["extra"].items():
                if isinstance(mval, dict):
                    normalized["mutations"]["extra"][mname] = {
                        "args": mval.get("args", {}),
                        "return_type": resolve_callable(mval.get("return_type")),
                        "resolver": resolve_callable(mval.get("resolver"))
                    }
                else:
                    normalized["mutations"]["extra"][mname] = resolve_callable(mval)

    return normalized
