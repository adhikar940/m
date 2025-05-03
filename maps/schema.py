import graphene
from .models import multiple_areas
from django.contrib.contenttypes.models import ContentType
from .types import MultipleAreasType

class mapsQuery(graphene.ObjectType):
    multiple_areas = graphene.List(
        MultipleAreasType,
        content_model=graphene.String(required=False),  ##  The model name - state,district,city etc.,.
        entity_field=graphene.String(required=False),   ## the model field to filter Ex statename if content_model=state
        entity_value=graphene.String(required=False)   ### the value of filed Ex : Andhra Pradesh if entity_field=statename
    )

    def resolve_multiple_areas(self, info, content_model=None, entity_field=None, entity_value=None):
        qs = multiple_areas.objects.all()
    
        if content_model:
            try:
                ct = ContentType.objects.get(app_label="area_pop", model=content_model)
                qs = qs.filter(content_type=ct)
            except ContentType.DoesNotExist:
                return multiple_areas.objects.none()

        results = list(qs)  # fetch the queryset first

        if entity_field and entity_value:
            # filter at Python level
            results = [
                obj for obj in results
                if hasattr(obj.entity, entity_field) and str(getattr(obj.entity, entity_field)) == str(entity_value)
            ]

        return results
