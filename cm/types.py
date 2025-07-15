import graphene
from graphene_django import DjangoObjectType
from .models import cm
from area_pop.models import State
from party.models import Party
from graphene.types.generic import GenericScalar

class PartyType(DjangoObjectType):
    class Meta:
        model = Party
        fields = "__all__"

class StateType(DjangoObjectType):
    class Meta:
        model = State
        fields = "__all__"

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

class TableCmType(graphene.ObjectType):
    """
    created for table data in UI
    """
    Name = graphene.String()
    State = graphene.String()
    Party = graphene.String()
    Gender = graphene.String()
    CasteCategory = graphene.String()
    Religion = graphene.String()
    PartyColor = graphene.String()

class CmCountsType(graphene.ObjectType):
    Party = GenericScalar()
    Gender = GenericScalar()
    CasteCategory = GenericScalar()
    Religion = GenericScalar()
    PartyColor = GenericScalar()