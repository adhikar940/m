import graphene
from graphene.types.generic import GenericScalar

class TableLoksabha(graphene.ObjectType):
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


class TableLoksabhaType(graphene.ObjectType):
    total_count = graphene.Int()
    TableLoksabha = graphene.List(TableLoksabha)
    

class LoksabhaCountsType(graphene.ObjectType):
    Party = GenericScalar()
    Gender = GenericScalar()
    CasteCategory = GenericScalar()
    Religion = GenericScalar()
    PartyColor = GenericScalar()

#### ENUMS

class SearchModeEnum(graphene.Enum):
    contains = "contains"
    exact = "exact"

class TableSearchFieldEnum(graphene.Enum):
    Name = "Name"
    Gender = "Gender"
    CasteCategory = "CasteCategory"
    Religion = "Religion"
    Party = "Party"
    PartyName = "PartyName"
    Constituency = "Constituency"
    State = "State"