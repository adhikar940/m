#from django.contrib.auth.models import User, Group
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


##########################################################################################

# FOR RAJYASABHA

class RajyasabhaSerializers(serializers.ModelSerializer):

    State = serializers.StringRelatedField()
    Party = serializers.StringRelatedField()

    class Meta:
        model = Rajyasabha
        fields = ['State', 'MP_name', 'party_name', 'Party', 'gender', 'fathers_Name', 'Spouse_Name', 'Highest_Education',
                  'University', 'photo', 'address', 'elected']

class State_RajyasabhaSerializer(serializers.ModelSerializer):

    Rajyasabha_Candidates = RajyasabhaSerializers(many=True, read_only=True)

    class Meta:
        model = State
        fields = ['State_name', 'Rajyasabha_Candidates']

#################################################################################

# LOKSABHA

class LokSabhaSerializers(serializers.ModelSerializer):

    State = serializers.StringRelatedField()
    Districts = serializers.StringRelatedField()
    Party = serializers.StringRelatedField()

    class Meta:
        model = LokSabha
        fields = ['State', 'Districts', 'MP_name', 'party_name', 'Party', 'gender', 'fathers_Name', 'Spouse_Name', 'Highest_Education',
                  'University', 'photo', 'address']

class State_loksabhaSerializer(serializers.ModelSerializer):

    Loksabha_Candidates = LokSabhaSerializers(many=True, read_only=True)

    class Meta:
        model = State
        fields = ['State_name', 'Loksabha_Candidates']

##########################################################################################################

# ASSEMBLY

class Legislative_AssemblySerializers(serializers.ModelSerializer):

    State = serializers.StringRelatedField()
    Districts = serializers.StringRelatedField()
    Party = serializers.StringRelatedField()

    class Meta:
        model = Legislative_Assembly
        fields = ['State', 'Districts', 'MLA_name', 'party_name', 'Party', 'gender', 'fathers_Name', 'Spouse_Name', 'Highest_Education',
                  'University', 'photo', 'address']

class State_AssemblySerializer(serializers.ModelSerializer):

    Assembly_Candidates = Legislative_AssemblySerializers(many=True, read_only=True)

    class Meta:
        model = State
        fields = ['State_name', 'Assembly_Candidates']

class District_Wise_AssemblySerializer(serializers.ModelSerializer):

    State = serializers.StringRelatedField()

    Assembly_Candidates = Legislative_AssemblySerializers(many=True, read_only=True)

    class Meta:
        model = Districts
        fields = ['State', 'District_name', 'Assembly_Candidates']

#################################################################################################

# FOR COUNCIL

class Legislative_councilsSerializer(serializers.ModelSerializer):

    State = serializers.StringRelatedField()
    Districts = serializers.StringRelatedField()
    Party = serializers.StringRelatedField()

    class Meta:
        model = Legislative_councils
        fields = ['State', 'MLC_name', 'elected', 'Districts', 'constituency_name', 'total_member']

class State_councilSerializer(serializers.ModelSerializer):

    Legislative_Council_Candidates = Legislative_councilsSerializer(many=True, read_only=True)

    class Meta:
        model = State
        fields = ['State_name', 'Legislative_Council_Candidates']

###########################################################################################


class Legislative_Council_PresenceSerializers(serializers.ModelSerializer):

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
        fields = ['State', 'start_date', 'End_date']


class Municipal_corporation_time_periodSerializers(serializers.ModelSerializer):

    State = serializers.StringRelatedField()
    Districts = serializers.StringRelatedField()
    City = serializers.StringRelatedField()

    class Meta:
        model = Municipal_corporation_time_period
        fields = ['State', 'District_name', 'City', 'corporation_name', 'start_date', 'End_date']


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
        fields = ['State', 'Districts', 'Mandal', 'panchayat_name', 'Sarpanch_name','gender','fathersName','SpouseName','HighestEducation','University','photo','address']


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
        fields = ['State', 'Districts', 'Mandal', 'panchayat_name', 'Ward_Member_Name', 'gender',
                  'fathersName', 'SpouseName', 'HighestEducation', 'University', 'photo', 'address']


class Corporation_Ward_NumberSerializers(serializers.ModelSerializer):

    State = serializers.StringRelatedField()
    Districts = serializers.StringRelatedField()
    City = serializers.StringRelatedField()

    class Meta:
        model = Corporation_Ward_Number
        fields = ['State', 'Districts', 'City', 'Ward_name', 'partyname', 'Corporator_name', 'partyname',
                  'gender', 'fathersName', 'SpouseName', 'HighestEducation', 'University', 'photo', 'address']


class Loksabha_SessionSerializers(serializers.ModelSerializer):
    loksabha = serializers.StringRelatedField()
    class Meta:
        model = Loksabha_Session
        fields = ['loksabha','date', 'session','link']

class Rajyasabha_SessionSerializers(serializers.ModelSerializer):
    rajyasabha = serializers.StringRelatedField()
    class Meta:
        model = Rajyasabha_Session
        fields = ['rajyasabha','date','session','link']

class Legislative_Assembly_SessionSerializers(serializers.ModelSerializer):
    legislative_assembly = serializers.StringRelatedField()
    class Meta:
        model = Legislative_Assembly_Session
        fields = ['legislative_assembly', 'date', 'session', 'link']

class Legislative_council_SessionSerializers(serializers.ModelSerializer):

    legislative_councils = serializers.StringRelatedField()

    class Meta:
        model = Legislative_council_Session
        fields = ['legislative_councils', 'date', 'session', 'link']

class PMSerializers(serializers.ModelSerializer):

    class Meta:
        model = PM
        fields = ['PM_name', 'date', 'session', 'link']


class PresidentSerializers(serializers.ModelSerializer):
    class Meta:
        model = President
        fields = ['President_name', 'date', 'session', 'link']

class Vice_PresidentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Vice_President
        fields = ['Vice_President_name', 'date', 'session', 'link']

class Rajyasabha_ChairmanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rajyasabha_Chairman
        fields = ['Rajyasabha_Chairman_name', 'date', 'session', 'link']

class Loksabha_ChairmanSerializers(serializers.ModelSerializer):
    class Meta:
        model = Loksabha_Chairman
        fields = ['Loksabha_Chairman_name', 'date', 'session', 'link']

class Loksabha_Complete_SessionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Loksabha_Complete_Session
        fields = ['Description', 'date', 'session', 'video_link']

class Rajyasabha_Complete_SessionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rajyasabha_Complete_Session
        fields = ['Description', 'date', 'session', 'video_link']




###########################################################################################################

class Current_Prime_MinisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Current_Prime_Minister
        fields = ['party_name', 'party', 'gender', 'fathers_Name', 'Spouse_Name', 'Highest_Education',
                  'University', 'photo', 'address', 'childhood_and_Education', 'About_Me', 'aims_Goal_and_Dream',
                  'Message_For_Followers']

class Current_PresidentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Current_President
        fields = ['party_name', 'party', 'gender', 'fathers_Name', 'Spouse_Name', 'Highest_Education',
                  'University', 'photo', 'address', 'childhood_and_Education', 'About_Me', 'aims_Goal_and_Dream',
                  'Message_For_Followers']

class Current_Vice_PresidentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Current_Vice_President
        fields = ['party_name', 'party', 'gender', 'fathers_Name', 'Spouse_Name', 'Highest_Education',
                  'University', 'photo', 'address', 'childhood_and_Education', 'About_Me', 'aims_Goal_and_Dream',
                  'Message_For_Followers']

class Current_Loksabha_SpeakerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Current_Loksabha_Speaker
        fields = ['party_name', 'party', 'gender', 'fathers_Name', 'Spouse_Name', 'Highest_Education',
                  'University', 'photo', 'address', 'childhood_and_Education', 'About_Me', 'aims_Goal_and_Dream',
                  'Message_For_Followers']

class Current_Loksabha_Deputy_SpeakerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Current_Loksabha_Deputy_Speaker
        fields = ['party_name', 'party', 'gender', 'fathers_Name', 'Spouse_Name', 'Highest_Education',
                  'University', 'photo', 'address', 'childhood_and_Education', 'About_Me', 'aims_Goal_and_Dream',
                  'Message_For_Followers']

class Current_Loksabha_Opposition_LeaderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Current_Loksabha_Opposition_Leader
        fields = ['party_name', 'party', 'gender', 'fathers_Name', 'Spouse_Name', 'Highest_Education',
                  'University', 'photo', 'address', 'childhood_and_Education', 'About_Me', 'aims_Goal_and_Dream',
                  'Message_For_Followers']

class Current_Rajyasabha_House_LeaderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Current_Rajyasabha_House_Leader
        fields = ['party_name', 'party', 'gender', 'fathers_Name', 'Spouse_Name', 'Highest_Education',
                  'University', 'photo', 'address', 'childhood_and_Education', 'About_Me', 'aims_Goal_and_Dream',
                  'Message_For_Followers']

class Current_Rajyasabha_Deputy_SpeakerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Current_Rajyasabha_Deputy_Speaker
        fields = ['party_name', 'party', 'gender', 'fathers_Name', 'Spouse_Name', 'Highest_Education',
                  'University', 'photo', 'address', 'childhood_and_Education', 'About_Me', 'aims_Goal_and_Dream',
                  'Message_For_Followers']

class Current_Rajyasabha_Opposition_LeaderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Current_Rajyasabha_Opposition_Leader
        fields = ['party_name', 'party', 'gender', 'fathers_Name', 'Spouse_Name', 'Highest_Education',
                  'University', 'photo', 'address', 'childhood_and_Education', 'About_Me', 'aims_Goal_and_Dream',
                  'Message_For_Followers']

#####################################################################################################################