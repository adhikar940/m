import graphene
from graphene_django import DjangoObjectType
from .models import cm

class cmType(DjangoObjectType):
    class Meta:
        model = cm
        fields = "__all__"
        filter_fields = {
            "id": ["exact"],
            "ispresent": ["exact"],
            "rulingstate__Statename": ["exact", "icontains"],  # <-- allow search by state name
            "party__partyname": ["exact", "icontains"],  # <-- allow search by party name
        }
        interfaces = (graphene.relay.Node,)