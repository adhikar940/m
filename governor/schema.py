from .types import GovernorType
import graphene
from graphene_django.filter import DjangoFilterConnectionField

class governorQuery(graphene.ObjectType):
    all_governors = DjangoFilterConnectionField(GovernorType)
