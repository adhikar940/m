from .types import cmType
import graphene
from graphene_django.filter import DjangoFilterConnectionField

class cmQuery(graphene.ObjectType):
    all_cms = DjangoFilterConnectionField(cmType)
