import graphene
from executive_leaders.schema import executiveleadersQuery
from maps.schema import mapsQuery
from governor.schema import governorQuery
from cm.schema import cmQuery
class Query(executiveleadersQuery, mapsQuery, governorQuery, cmQuery, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)