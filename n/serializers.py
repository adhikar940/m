from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . models import *


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name']


class BiharCandidateSerializers(serializers.ModelSerializer):

    State = serializers.StringRelatedField()
    Districts = serializers.StringRelatedField()

    class Meta:
        model = BiharCandidate
        fields = ['State', 'partyname', 'Candidate', 'constituency_name', 'Districts', 'Residence', 'Photo']


class DubbakaCandidateSerializers(serializers.ModelSerializer):
    State = serializers.StringRelatedField()
    Districts = serializers.StringRelatedField()

    class Meta:
        model = DubbakaCandidate
        fields = ['State', 'partyname', 'Candidate', 'constituency_name', 'Districts', 'Residence', 'Photo']


class PartySerializers(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ['party_status', 'partyname', 'abbreviation', 'President', 'founder', 'chairperson', 'founded_date', 'headquarters', 'seats_in_rajyasabha', 'seats_in_loksabha', 'party_symbol', 'founderPhoto', 'chairpersonPhoto']


class Bihar_Coalition_PartySerializers(serializers.ModelSerializer):
    class Meta:
        model = Bihar_Coalition_Party
        fields = ['party_status', 'partyname', 'abbreviation', 'President', 'founder', 'chairperson', 'founded_date', 'headquarters', 'seats_in_rajyasabha', 'seats_in_loksabha', 'party_symbol', 'founderPhoto', 'chairpersonPhoto']


class DubbakaRunnersSerializers(serializers.ModelSerializer):

    State = serializers.StringRelatedField()
    Districts = serializers.StringRelatedField()

    class Meta:
        model = DubbakaRunners
        fields = ['State', 'partyname', 'Candidate', 'constituency_name', 'Districts', 'Residence', 'Photo', 'total_contested', 'no_of_votes']


class DubbakaWinnersSerializers(serializers.ModelSerializer):

    State = serializers.StringRelatedField()
    Districts = serializers.StringRelatedField()

    class Meta:
        model = DubbakaWinners
        fields = ['State', 'partyname', 'Candidate', 'constituency_name', 'Districts', 'Residence', 'Photo', 'total_contested', 'no_of_votes']


class BiharWinnersSerializers(serializers.ModelSerializer):
    State = serializers.StringRelatedField()
    Districts = serializers.StringRelatedField()

    class Meta:
        model = BiharWinners
        fields = ['State', 'partyname', 'Candidate', 'constituency_name', 'Districts', 'Residence', 'Photo', 'total_contested', 'no_of_votes']


class BiharRunnersSerializers(serializers.ModelSerializer):

    State = serializers.StringRelatedField()
    Districts = serializers.StringRelatedField()

    class Meta:
        model = BiharRunners
        fields = ['State', 'partyname', 'Candidate', 'constituency_name', 'Districts', 'Residence', 'Photo', 'total_contested', 'no_of_votes']


class statesSerializers(serializers.ModelSerializer):

    State = serializers.StringRelatedField()

    class Meta:
        model = States
        fields = ['State', 'capital', 'chief_minister', 'chief_minister_Photo', 'Governor', 'Governor_Photo']



class LeadingSeatsSerializers(serializers.ModelSerializer):
    class Meta:
        model = LeadingSeats
        fields = ['MGB', 'NDA', 'LJP', 'Others']



class RajyasabhaSerializers(serializers.ModelSerializer):

    State = serializers.StringRelatedField()

    class Meta:
        model = Rajyasabha
        fields = ['State', 'MPname', 'partyname', 'gender', 'fathersName', 'SpouseName', 'HighestEducation', 'University', 'photo', 'address']


class LokSabhaSerializers(serializers.ModelSerializer):

    State = serializers.StringRelatedField()
    Districts = serializers.StringRelatedField()

    class Meta:
        model = LokSabha
        fields = ['State', 'MPname', 'partyname', 'Districts', 'constituency_name', 'gender', 'fathersName', 'SpouseName', 'HighestEducation', 'University', 'photo', 'address']


class Legislative_AssemblySerializers(serializers.ModelSerializer):

    State = serializers.StringRelatedField()
    Districts = serializers.StringRelatedField()

    class Meta:
        model = Legislative_Assembly
        fields = ['State', 'MLA_name', 'partyname', 'Districts', 'constituency_name', 'gender', 'fathersName', 'SpouseName', 'HighestEducation', 'University', 'photo', 'address']


class Legislative_CouncilSerializers(serializers.ModelSerializer):

    State = serializers.StringRelatedField()

    class Meta:
        model = Legislative_Council_Presence
        fields = ['State',  'presence']



class Assembly_time_periodSerializers(serializers.ModelSerializer):

    State = serializers.StringRelatedField()

    class Meta:
        model = Assembly_time_period
        fields = ['State', 'start_date', 'End_date']


class Panchayat_time_periodSerializers(serializers.ModelSerializer):

    State = serializers.StringRelatedField()

    class Meta:
        model = Panchayat_time_period
        fields = ['State', 'start_date', 'End_date','partyname','gender','fathersName','SpouseName','HighestEducation','University','photo','address']


class Municipal_corporation_time_periodSerializers(serializers.ModelSerializer):

    State = serializers.StringRelatedField()
    Districts = serializers.StringRelatedField()
    City = serializers.StringRelatedField()

    class Meta:
        model = Municipal_corporation_time_period
        fields = ['State', 'District_name', 'City', 'corporation_name', 'start_date', 'End_date','partyname','gender','fathersName','SpouseName','HighestEducation','University','photo','address']


class StateSerializers(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = ['State_name']


class DistrictsSerializers(serializers.ModelSerializer):

    State = serializers.StringRelatedField()

    class Meta:
        model = Districts
        fields = ['State', 'District_name']


class CitySerializers(serializers.ModelSerializer):

    State = serializers.StringRelatedField()
    Districts = serializers.StringRelatedField()

    class Meta:
        model = City
        fields = ['State', 'Districts', 'City_name']


class Grama_panchayatSerializers(serializers.ModelSerializer):

    State = serializers.StringRelatedField()
    Districts = serializers.StringRelatedField()

    class Meta:
        model = Grama_panchayat
        fields = ['State', 'Districts', 'Mandal', 'panchayat_name', 'Sarpanch_name','partyname','gender','fathersName','SpouseName','HighestEducation','University','photo','address']


class CorporationSerializers(serializers.ModelSerializer):

    State = serializers.StringRelatedField()
    Districts = serializers.StringRelatedField()
    City = serializers.StringRelatedField()

    class Meta:
        model = Corporation
        fields = ['State', 'Districts', 'City', 'Corporation_name', 'partyname', 'Mayor_name','partyname','gender','fathersName','SpouseName','HighestEducation','University','photo','address']


class Panchayat_Ward_NumberSerializers(serializers.ModelSerializer):

    State = serializers.StringRelatedField()
    Districts = serializers.StringRelatedField()

    class Meta:
        model = Panchayat_Ward_Number
        fields = ['State', 'Districts', 'Mandal', 'panchayat_name', 'Ward_Member_Name','partyname','gender','fathersName','SpouseName','HighestEducation','University','photo','address']


class Corporation_Ward_NumberSerializers(serializers.ModelSerializer):

    State = serializers.StringRelatedField()
    Districts = serializers.StringRelatedField()
    City = serializers.StringRelatedField()

    class Meta:
        model = Corporation_Ward_Number
        fields = ['State', 'Districts', 'City', 'Ward_name', 'partyname', 'Corporator_name','partyname','gender','fathersName','SpouseName','HighestEducation','University','photo','address']
