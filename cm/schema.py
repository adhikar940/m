from .types import cmType,TableCmType,CmCountsType
import graphene
from graphene_django.filter import DjangoFilterConnectionField
from .models import cm

class cmQuery(graphene.ObjectType):
    all_cms = DjangoFilterConnectionField(cmType)
    all_cms_table = graphene.List(
        TableCmType,
        ispresent=graphene.Boolean(required=False)
    )

    def resolve_all_cms_table(self, info,ispresent=None):
        queryset = cm.objects.all()
        if ispresent is not None:
            queryset = queryset.filter(ispresent=ispresent)
        return [
            {
                "Name": cm_instance.name,
                "State": cm_instance.rulingstate.Statename if cm_instance.rulingstate else None,
                "Party": cm_instance.party.abbreviation if cm_instance.party else None,
                "Gender": cm_instance.gender,
                "CasteCategory": cm_instance.caste_category,
                "Religion": cm_instance.religion,
                "PartyColor": cm_instance.party.party_color if cm_instance.party else None
            }
            for cm_instance in queryset
        ]
    
    cm_counts = graphene.Field(
        CmCountsType,
        ispresent=graphene.Boolean(required=False)
    )

    def resolve_cm_counts(self, info, ispresent=None):
        from django.db.models import Count

        queryset = cm.objects.all()
        if ispresent is not None:
            queryset = queryset.filter(ispresent=ispresent)

        def get_count_dict(qs, field_name):
            return {
                item[field_name] or "Unknown": item["count"]
                for item in qs
            }
        
        def get_party_color_dict(qs):
            return {
                item["party__abbreviation"] or "Unknown": item["party__party_color"] or "#000000"
                for item in qs
            }
            
        party_qs = queryset.values("party__abbreviation", "party__party_color").annotate(count=Count("id"))
        gender_qs = queryset.values("gender").annotate(count=Count("id"))
        caste_qs = queryset.values("caste_category").annotate(count=Count("id"))
        religion_qs = queryset.values("religion").annotate(count=Count("id"))

        return CmCountsType(
            Party=get_count_dict(party_qs, "party__abbreviation"),
            PartyColor=get_party_color_dict(party_qs),
            Gender=get_count_dict(gender_qs, "gender"),
            CasteCategory=get_count_dict(caste_qs, "caste_category"),
            Religion=get_count_dict(religion_qs, "religion"),
        )