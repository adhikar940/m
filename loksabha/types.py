import graphene
from graphene.types.generic import GenericScalar

class TableLoksabhaType(graphene.ObjectType):
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

class LoksabhaCountsType(graphene.ObjectType):
    Party = GenericScalar()
    Gender = GenericScalar()
    CasteCategory = GenericScalar()
    Religion = GenericScalar()
    PartyColor = GenericScalar()