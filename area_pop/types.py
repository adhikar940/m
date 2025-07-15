from graphene_django import DjangoObjectType
from .models import State

class StateType(DjangoObjectType):
    class Meta:
        model = State
        fields = "__all__"