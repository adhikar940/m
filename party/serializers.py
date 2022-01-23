from . models import *
from rest_framework import serializers
class PSerializers1(serializers.ModelSerializer):
    class Meta:
        model = Party1
        fields = ['id','partyname', 'abbreviation','actvated']
class PartySerializers1(serializers.ModelSerializer):
    class Meta:
        model = Party1
        fields = ['id','party_status', 'partyname', 'abbreviation', 'President', 'founder', 'chairperson', 'founded_date',
                  'headquarters', 'seats_in_rajyasabha', 'seats_in_loksabha', 'party_symbol', 'founderPhoto',
                  'chairpersonPhoto','actvated']
class statepartyactivateSerializers1(serializers.ModelSerializer):
    state = serializers.StringRelatedField()
    party = serializers.StringRelatedField()
    class Meta:
        model = districtpartyactivate
        fields = ['party','state','email']
class districtpartyactivateSerializers1(serializers.ModelSerializer):
    state = serializers.StringRelatedField()
    district = serializers.StringRelatedField()
    class Meta:
        model = statepartyactivate1
        fields = ['party','district','email']
