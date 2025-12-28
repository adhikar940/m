import graphene
from graphene_django import DjangoObjectType
from .models import *
import django_filters
from graphene_django.filter import DjangoFilterConnectionField
from graphene import relay


# Define GraphQL Type with Relay Node
class ExecutiveLeaderType(DjangoObjectType):
    class Meta:
        model = ExecutiveLeader
        interfaces = (relay.Node,)  

# Define Filters
class ExecutiveLeaderFilter(django_filters.FilterSet):
    is_present = django_filters.BooleanFilter()  
    leader_type = django_filters.CharFilter(method="filter_leader_type") 

    class Meta:
        model = ExecutiveLeader
        fields = {
            'ruling_periods': ['exact', 'icontains']       
              }
    def filter_leader_type(self, queryset, name, value):
        values = value.split(",")  # Split values on comma (e.g., "pm,president")
        return queryset.filter(leader_type__in=values)

# Define Query Class
class executiveleadersQuery(graphene.ObjectType):
    execLeaderDetails = DjangoFilterConnectionField(ExecutiveLeaderType, filterset_class=ExecutiveLeaderFilter)


'''class executive_leader_details(DjangoObjectType):
    class Meta:
        model = executive_leader
        fields = "__all__"  


class Query(graphene.ObjectType):
    execLeaderDetails = graphene.List(executive_leader_details)
    def resolve_execLeaderDetails(root, info):
        return executive_leader.objects.all()'''
