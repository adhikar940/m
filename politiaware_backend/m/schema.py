import graphene
from governor.schema import governorQuery
from cm.schema import cmQuery
from loksabha.schema import loksabhaQuery
from person.schema import EnumQuery

from generic_graphql import generate_generic_graphql
from graphql_conf.graphql_conf import GRAPHQL_CONF

# Dynamically generate generic queries and mutations from config
GenericQuery, GenericMutation = generate_generic_graphql(GRAPHQL_CONF)

class Query(
    GenericQuery,
    EnumQuery,
    governorQuery,
    cmQuery,
    loksabhaQuery,
    graphene.ObjectType
):
    pass

class Mutation(
    GenericMutation,
    graphene.ObjectType
):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)