from .types import TableLoksabhaType,TableLoksabha,TableSearchFieldEnum,SearchModeEnum
import graphene
from .models import LokSabhaMP
from utils.graphql_utils import graphql_search, graphql_orderby

class loksabhaQuery(graphene.ObjectType):   
    lokSabhaMpsTable = graphene.Field(
        TableLoksabhaType, 
        search=graphene.List(graphene.String),
        search_fields=graphene.List(TableSearchFieldEnum),
        search_mode=graphene.Argument(SearchModeEnum, default_value=SearchModeEnum.contains),
        order_by=graphene.List(TableSearchFieldEnum),
        offset=graphene.Int(),
        limit=graphene.Int()
    )
    
    def resolve_lokSabhaMpsTable(                             
        self, info, search=None, search_fields=None, order_by=None, offset=0, limit=10,search_mode=SearchModeEnum.contains
    ):
  
        queryset = LokSabhaMP.objects.filter(ispresent=True).select_related(
            "Party", "constituency__State"
        )
        base_fields = {
        "Name": "name",
        "Gender": "gender",
        "CasteCategory": "caste_category",
        "Religion": "religion",
        "Party": "Party__abbreviation",
        "PartyName": "Party__partyname",
        "Constituency": "constituency__LoksabhaConstituencyName",
        "State": "constituency__State__Statename",
        }
        queryset = graphql_search(base_fields, search, search_fields, search_mode, queryset)              

        TotalCount = queryset.count()

        order_fields_map = {
            "Name": "name",
            "Gender": "gender",
            "CasteCategory": "caste_category",
            "Religion": "religion",
            "Party": "Party__abbreviation",
            "PartyName": "Party__partyname", 
            "Constituency": "constituency__LoksabhaConstituencyName",
            "State": "constituency__State__Statename"
        }
        # queryset = graphql_orderby(queryset, order_by, order_fields_map)
        # 🔃 Apply ordering
        queryset = graphql_orderby(queryset, order_by, order_fields_map)
                
        # 🧾 Apply pagination
        queryset = queryset[offset:offset + limit]

        return TableLoksabhaType(
                TableLoksabha=[
                    TableLoksabha(
                        Name=mp.name,
                        State=mp.constituency.State.Statename if mp.constituency and mp.constituency.State else None,
                        Party=mp.Party.abbreviation if mp.Party else None,
                        Gender=mp.gender,
                        CasteCategory=mp.caste_category,
                        Religion=mp.religion,
                        PartyColor=mp.Party.party_color if mp.Party else None
                    )
                    for mp in queryset
                ],
                total_count=TotalCount
            )


