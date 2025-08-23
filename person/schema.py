from graphene import ObjectType
from .enums import CasteCategoryEnum, GenderEnum, ReligionEnum
import graphene
from .types import CasteCategoryGQL,GenderGQL,ReligionGQL

class EnumQuery(graphene.ObjectType):
    caste_categories = graphene.List(CasteCategoryGQL)
    genders = graphene.List(GenderGQL)
    religions = graphene.List(ReligionGQL)

    def resolve_caste_categories(self, info):
        return [e.value for e in CasteCategoryEnum]

    def resolve_genders(self, info):
        return [e.value for e in GenderEnum]

    def resolve_religions(self, info):
        return [e.value for e in ReligionEnum]