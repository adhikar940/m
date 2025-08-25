import graphene
from .enums import CasteCategoryEnum, GenderEnum, ReligionEnum

CasteCategoryGQL = graphene.Enum.from_enum(CasteCategoryEnum)
GenderGQL = graphene.Enum.from_enum(GenderEnum)
ReligionGQL = graphene.Enum.from_enum(ReligionEnum)