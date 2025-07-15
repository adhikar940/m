from django.db.models import Q
from .types import TableLoksabhaType
import graphene
from .models import LokSabhaMP

class loksabhaQuery(graphene.ObjectType):   
    lok_sabha_mps_table = graphene.List(
        TableLoksabhaType, 
        search=graphene.String(),
        search_fields=graphene.List(graphene.String),
        order_by=graphene.List(graphene.String),
        offset=graphene.Int(),
        limit=graphene.Int()
    )

    def resolve_paginated_lok_sabha_mps(                             
        self, info, search=None, search_fields=None, order_by=None, offset=0, limit=10
    ):
        
        queryset = LokSabhaMP.objects.filter(ispresent=True).select_related(
            "Party", "constituency__State"
        )

        # 🔍 Default search fields
        all_search_fields = {
            "MPName": "MPName__icontains",
            "Gender": "gender__icontains",
            "CasteCategory": "caste_category__icontains",
            "Religion": "religion__icontains",
            "Party": "Party__abbreviation__icontains",
            "PartyName": "Party__party_name__icontains",
            "PartyColor": "Party__party_color__icontains",
            "Constituency": "constituency__LoksabhaConstituencyName__icontains",
            "State": "constituency__State__Statename__icontains",
        }

        # 🔍 Apply search filters
        if search:
            fields = search_fields or list(all_search_fields.keys())
            q_objects = Q()
            for field in fields:
                if field in all_search_fields:
                    q_objects |= Q(**{all_search_fields[field]: search})
            queryset = queryset.filter(q_objects)

        # 🔃 Apply ordering
        if order_by:
            queryset = queryset.order_by(*order_by)

        # 🧾 Apply pagination
        queryset = queryset[offset:offset + limit]

        return [
                TableLoksabhaType(
                Name=mp.MPName,
                State=mp.constituency.State.Statename if mp.constituency and mp.constituency.State else None,
                Party=mp.Party.abbreviation if mp.Party else None,
                Gender=mp.gender,
                CasteCategory=mp.caste_category,
                Religion=mp.religion,
                PartyColor=mp.Party.party_color if mp.Party else None
            )
            for mp in queryset
        ]

