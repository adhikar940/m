import graphene
from graphene_django import DjangoObjectType
from .models import governor

class GovernorType(DjangoObjectType):
    class Meta:
        model = governor
        fields = "__all__"
        filter_fields = {
            "id": ["exact"],
            "ispresent": ["exact"],
            "rulingstate__Statename": ["exact", "icontains"],  # <-- allow search by state name
        }
        interfaces = (graphene.relay.Node,)
