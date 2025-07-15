import graphene
from maps.schema import mapsQuery
from governor.schema import governorQuery
from cm.schema import cmQuery
from loksabha.schema import loksabhaQuery
class Query(mapsQuery, governorQuery, cmQuery, loksabhaQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)