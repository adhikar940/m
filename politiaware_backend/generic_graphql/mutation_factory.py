"""
Dynamic Mutation Generator for generic_graphql.
Builds create, update, delete, and extra mutations with validation and hooks.
"""

from typing import Any, Dict, List, Optional, Tuple, Type
import graphene
from django.core.exceptions import ValidationError
from django.db import models, transaction

from .model_loader import get_field_by_name
from .field_mapper import django_field_to_graphene_type
from .type_factory import (
    DeletePayload,
    get_or_create_django_type,
    get_or_create_payload_type
)
from .input_factory import get_or_create_input_type


def _format_mutation_name(model_name: str, action: str) -> str:
    """Formats mutation name e.g. createLokSabhaMp, updateLokSabhaMp, deleteLokSabhaMp."""
    clean_name = model_name[0].upper() + model_name[1:] if model_name else ""
    return f"{action.lower()}{clean_name}"


def _get_clean_exclude_fields(model_cls: Type[models.Model], input_data: Dict[str, Any], required_cols: List[str]) -> List[str]:
    """
    Determines which fields to exclude from full_clean validation if not provided in input_data.
    Excludes nullable/optional unsupplied fields (like unsupplied ImageFields/FileFields with null=True).
    """
    exclude = []
    for field in model_cls._meta.get_fields():
        if not hasattr(field, "name") or field.name in input_data or field.name in required_cols:
            continue
        # If field allows null or has default, exclude from strict validation if not provided
        if getattr(field, "null", False) or getattr(field, "blank", False) or getattr(field, "has_default", lambda: False)():
            exclude.append(field.name)
    return exclude


def _assign_model_fields(instance: models.Model, data_dict: Dict[str, Any], allowed_cols: List[str]):
    """
    Safely assigns dictionary values to a Django model instance,
    handling ForeignKeys (assigning _id) and regular fields.
    """
    for col, val in data_dict.items():
        if col not in allowed_cols:
            continue
        field_obj = get_field_by_name(instance.__class__, col)

        if isinstance(field_obj, (models.ForeignKey, models.OneToOneField)):
            if isinstance(val, (int, str)) or val is None:
                setattr(instance, f"{field_obj.name}_id", val)
            else:
                setattr(instance, field_obj.name, val)
        else:
            setattr(instance, col, val)


def create_dynamic_create_mutation(
    model_cls: Type[models.Model],
    create_cols: List[str],
    return_cols: Any,
    required_cols: List[str],
    before_save: Optional[Any] = None,
    after_save: Optional[Any] = None,
    custom_mutate: Optional[Any] = None,
    mutation_class_name: Optional[str] = None
) -> Type[graphene.Mutation]:
    """
    Generates a dynamic Graphene Create Mutation class.
    """
    class_name = mutation_class_name or f"Create_{model_cls._meta.app_label}_{model_cls.__name__}_Mutation"
    django_type = get_or_create_django_type(model_cls, return_cols=return_cols)
    payload_type = get_or_create_payload_type(model_cls, django_type)
    input_type = get_or_create_input_type(model_cls, create_cols, is_update=False, required_cols=required_cols)

    class DynamicArguments:
        input = input_type(required=True)

    def mutate_func(cls, root, info, **kwargs):
        if custom_mutate:
            return custom_mutate(root, info, **kwargs)

        input_data = kwargs.get("input") or {}
        instance = model_cls()

        try:
            with transaction.atomic():
                _assign_model_fields(instance, input_data, create_cols)

                if before_save:
                    before_save(instance, info, input_data)

                # Validate model with unprovided nullable fields excluded
                exclude_fields = _get_clean_exclude_fields(model_cls, input_data, required_cols)
                instance.full_clean(exclude=exclude_fields if exclude_fields else None)
                instance.save()

                if after_save:
                    after_save(instance, info)

            res_kwargs = {
                "success": True,
                "errors": None,
                "data": instance,
                model_cls.__name__.lower(): instance
            }
            return payload_type(**res_kwargs)
        except ValidationError as ve:
            errors = []
            if hasattr(ve, "message_dict"):
                for f, msgs in ve.message_dict.items():
                    errors.extend([f"{f}: {m}" for m in msgs])
            else:
                errors = list(ve.messages)
            return payload_type(success=False, errors=errors, data=None)
        except Exception as e:
            return payload_type(success=False, errors=[str(e)], data=None)

    mutation_cls = type(
        class_name,
        (graphene.Mutation,),
        {
            "Arguments": DynamicArguments,
            "success": graphene.Boolean(required=True),
            "errors": graphene.List(graphene.String),
            "data": graphene.Field(django_type),
            model_cls.__name__.lower(): graphene.Field(django_type),
            "mutate": classmethod(mutate_func)
        }
    )
    return mutation_cls


def create_dynamic_update_mutation(
    model_cls: Type[models.Model],
    update_cols: List[str],
    return_cols: Any,
    pk_field_name: str = "id",
    before_save: Optional[Any] = None,
    after_save: Optional[Any] = None,
    custom_mutate: Optional[Any] = None,
    mutation_class_name: Optional[str] = None
) -> Type[graphene.Mutation]:
    """
    Generates a dynamic Graphene Update Mutation class.
    """
    class_name = mutation_class_name or f"Update_{model_cls._meta.app_label}_{model_cls.__name__}_Mutation"
    django_type = get_or_create_django_type(model_cls, return_cols=return_cols)
    payload_type = get_or_create_payload_type(model_cls, django_type)
    input_type = get_or_create_input_type(model_cls, update_cols, is_update=True)

    pk_field = get_field_by_name(model_cls, pk_field_name)
    pk_graphene_type = django_field_to_graphene_type(pk_field)

    class DynamicArguments:
        pass

    setattr(DynamicArguments, pk_field_name, pk_graphene_type(required=True))
    setattr(DynamicArguments, "input", input_type(required=True))

    def mutate_func(cls, root, info, **kwargs):
        if custom_mutate:
            return custom_mutate(root, info, **kwargs)

        pk_val = kwargs.get(pk_field_name)
        input_data = kwargs.get("input") or {}

        try:
            instance = model_cls.objects.filter(**{pk_field_name: pk_val}).first()
            if not instance:
                return payload_type(
                    success=False,
                    errors=[f"{model_cls.__name__} with {pk_field_name}={pk_val} does not exist."],
                    data=None
                )

            with transaction.atomic():
                _assign_model_fields(instance, input_data, update_cols)

                if before_save:
                    before_save(instance, info, input_data)

                # Validate only updated fields or full model
                exclude_fields = _get_clean_exclude_fields(model_cls, input_data, [])
                instance.full_clean(exclude=exclude_fields if exclude_fields else None)
                instance.save()

                if after_save:
                    after_save(instance, info)

            res_kwargs = {
                "success": True,
                "errors": None,
                "data": instance,
                model_cls.__name__.lower(): instance
            }
            return payload_type(**res_kwargs)
        except ValidationError as ve:
            errors = []
            if hasattr(ve, "message_dict"):
                for f, msgs in ve.message_dict.items():
                    errors.extend([f"{f}: {m}" for m in msgs])
            else:
                errors = list(ve.messages)
            return payload_type(success=False, errors=errors, data=None)
        except Exception as e:
            return payload_type(success=False, errors=[str(e)], data=None)

    mutation_cls = type(
        class_name,
        (graphene.Mutation,),
        {
            "Arguments": DynamicArguments,
            "success": graphene.Boolean(required=True),
            "errors": graphene.List(graphene.String),
            "data": graphene.Field(django_type),
            model_cls.__name__.lower(): graphene.Field(django_type),
            "mutate": classmethod(mutate_func)
        }
    )
    return mutation_cls


def create_dynamic_delete_mutation(
    model_cls: Type[models.Model],
    pk_field_name: str = "id",
    before_delete: Optional[Any] = None,
    after_delete: Optional[Any] = None,
    custom_mutate: Optional[Any] = None,
    mutation_class_name: Optional[str] = None
) -> Type[graphene.Mutation]:
    """
    Generates a dynamic Graphene Delete Mutation class.
    """
    class_name = mutation_class_name or f"Delete_{model_cls._meta.app_label}_{model_cls.__name__}_Mutation"
    pk_field = get_field_by_name(model_cls, pk_field_name)
    pk_graphene_type = django_field_to_graphene_type(pk_field)

    class DynamicArguments:
        pass

    setattr(DynamicArguments, pk_field_name, pk_graphene_type(required=True))

    def mutate_func(cls, root, info, **kwargs):
        if custom_mutate:
            return custom_mutate(root, info, **kwargs)

        pk_val = kwargs.get(pk_field_name)
        try:
            instance = model_cls.objects.filter(**{pk_field_name: pk_val}).first()
            if not instance:
                return DeletePayload(
                    success=False,
                    errors=[f"{model_cls.__name__} with {pk_field_name}={pk_val} does not exist."],
                    id=pk_val
                )

            with transaction.atomic():
                if before_delete:
                    before_delete(instance, info)

                instance.delete()

                if after_delete:
                    after_delete(pk_val, info)

            return DeletePayload(success=True, errors=None, id=pk_val)
        except Exception as e:
            return DeletePayload(success=False, errors=[str(e)], id=pk_val)

    mutation_cls = type(
        class_name,
        (graphene.Mutation,),
        {
            "Arguments": DynamicArguments,
            "success": graphene.Boolean(required=True),
            "errors": graphene.List(graphene.String),
            "id": graphene.ID(),
            "mutate": classmethod(mutate_func)
        }
    )
    return mutation_cls


def build_model_mutations(
    model_name: str,
    normalized_config: Dict[str, Any]
) -> Dict[str, Type[graphene.Mutation]]:
    """
    Builds all mutations (create, update, delete, extra) for a single model.
    Returns: { mutation_field_name: MutationClass }
    """
    mutations_dict = {}
    model_cls = normalized_config["model_cls"]
    mutations_cfg = normalized_config.get("mutations") or {}

    # 1. Create Mutation
    create_cfg = mutations_cfg.get("create")
    if create_cfg and create_cfg.get("enabled", True):
        mutation_name = create_cfg.get("name") or _format_mutation_name(model_cls.__name__, "create")
        create_mut = create_dynamic_create_mutation(
            model_cls=model_cls,
            create_cols=create_cfg.get("create_cols", []),
            return_cols=create_cfg.get("return_cols", "__all__"),
            required_cols=create_cfg.get("required_cols", []),
            before_save=create_cfg.get("before_save"),
            after_save=create_cfg.get("after_save"),
            custom_mutate=create_cfg.get("mutate")
        )
        mutations_dict[mutation_name] = create_mut.Field()

    # 2. Update Mutation
    update_cfg = mutations_cfg.get("update")
    if update_cfg and update_cfg.get("enabled", True):
        mutation_name = update_cfg.get("name") or _format_mutation_name(model_cls.__name__, "update")
        update_mut = create_dynamic_update_mutation(
            model_cls=model_cls,
            update_cols=update_cfg.get("update_cols", []),
            return_cols=update_cfg.get("return_cols", "__all__"),
            pk_field_name=update_cfg.get("pk", "id"),
            before_save=update_cfg.get("before_save"),
            after_save=update_cfg.get("after_save"),
            custom_mutate=update_cfg.get("mutate")
        )
        mutations_dict[mutation_name] = update_mut.Field()

    # 3. Delete Mutation
    delete_cfg = mutations_cfg.get("delete")
    if delete_cfg and delete_cfg.get("enabled", True):
        mutation_name = delete_cfg.get("name") or _format_mutation_name(model_cls.__name__, "delete")
        delete_mut = create_dynamic_delete_mutation(
            model_cls=model_cls,
            pk_field_name=delete_cfg.get("pk", "id"),
            before_delete=delete_cfg.get("before_delete"),
            after_delete=delete_cfg.get("after_delete"),
            custom_mutate=delete_cfg.get("mutate")
        )
        mutations_dict[mutation_name] = delete_mut.Field()

    # 4. Extra Mutations for this model
    extra_cfg = mutations_cfg.get("extra") or {}
    for extra_name, extra_val in extra_cfg.items():
        if isinstance(extra_val, type) and issubclass(extra_val, graphene.Mutation):
            mutations_dict[extra_name] = extra_val.Field()
        elif hasattr(extra_val, "Field"):
            mutations_dict[extra_name] = extra_val.Field()
        elif isinstance(extra_val, dict):
            args_dict = extra_val.get("args") or {}
            custom_resolver = extra_val.get("resolver")
            return_type = extra_val.get("return_type") or graphene.Boolean

            class DynamicExtraArgs:
                pass
            for aname, atype in args_dict.items():
                setattr(DynamicExtraArgs, aname, atype)

            def make_extra_mutate(res_fn):
                def mutate_wrapper(cls, root, info, **kwargs):
                    if res_fn:
                        return res_fn(root, info, **kwargs)
                    return True
                return mutate_wrapper

            extra_mut_cls = type(
                f"Extra_{model_cls._meta.app_label}_{extra_name}_Mutation",
                (graphene.Mutation,),
                {
                    "Arguments": DynamicExtraArgs,
                    "result": return_type(),
                    "mutate": classmethod(make_extra_mutate(custom_resolver))
                }
            )
            mutations_dict[extra_name] = extra_mut_cls.Field()

    return mutations_dict
