import graphene
from area_pop.models import area, population, State
from graphene.types.generic import GenericScalar
from graphene_django import DjangoObjectType
from .models import multiple_areas
from django.contrib.contenttypes.models import ContentType

class AreaType(DjangoObjectType):
    class Meta:
        model = area
        fields = "__all__"

class PopulationType(DjangoObjectType):
    class Meta:
        model = population
        fields = "__all__"


class MultipleAreasType(DjangoObjectType):
    entity = GenericScalar()
    area = graphene.Field(AreaType)
    population = graphene.Field(PopulationType)
    boundary = GenericScalar()
    class Meta: 
        model = multiple_areas
        exclude = ("boundary",) 

    def resolve_entity(self, info):
        if self.entity:
            output = {}
            for field in self.entity._meta.fields:
                if field.name == 'id':
                    continue  
                try:
                    output[field.name] = getattr(self.entity, field.name)
                except AttributeError:
                    output[field.name] = None
            return output
        return None


    def resolve_area(self, info):
        return area.objects.filter(content_type=self.content_type, object_id=self.object_id).first()


    def resolve_population(self, info):
        return population.objects.filter(
            content_type=self.content_type,
            object_id=self.object_id,
            census_year=2011
        ).first()
    def resolve_boundary(self, info):
        if self.boundary:
            return self.boundary.geojson  # 👈 convert MultiPolygon to GeoJSON
        return None