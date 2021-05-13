from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . models import *


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'name']

'''
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
'''

class PartySerializers(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ['party_status', 'partyname', 'abbreviation', 'President', 'founder', 'chairperson', 'founded_date',
                  'headquarters', 'seats_in_rajyasabha', 'seats_in_loksabha', 'party_symbol', 'founderPhoto',
                  'chairpersonPhoto']
'''

class Bihar_Coalition_PartySerializers(serializers.ModelSerializer):
    class Meta:
        model = Bihar_Coalition_Party
        fields = ['party_status', 'partyname', 'abbreviation', 'President', 'founder', 'chairperson', 'founded_date',
                  'headquarters', 'seats_in_rajyasabha', 'seats_in_loksabha', 'party_symbol', 'founderPhoto',
                  'chairpersonPhoto']


class DubbakaRunnersSerializers(serializers.ModelSerializer):

    State = serializers.StringRelatedField()
    Districts = serializers.StringRelatedField()

    class Meta:
        model = DubbakaRunners
        fields = ['State', 'partyname', 'Candidate', 'constituency_name', 'Districts', 'Residence', 'Photo',
                  'total_contested', 'no_of_votes']


class DubbakaWinnersSerializers(serializers.ModelSerializer):

    State = serializers.StringRelatedField()
    Districts = serializers.StringRelatedField()

    class Meta:
        model = DubbakaWinners
        fields = ['State', 'partyname', 'Candidate', 'constituency_name', 'Districts', 'Residence', 'Photo',
                  'total_contested', 'no_of_votes']


class BiharWinnersSerializers(serializers.ModelSerializer):
    State = serializers.StringRelatedField()
    Districts = serializers.StringRelatedField()

    class Meta:
        model = BiharWinners
        fields = ['State', 'partyname', 'Candidate', 'constituency_name', 'Districts', 'Residence', 'Photo',
                  'total_contested', 'no_of_votes']


class BiharRunnersSerializers(serializers.ModelSerializer):

    State = serializers.StringRelatedField()
    Districts = serializers.StringRelatedField()

    class Meta:
        model = BiharRunners
        fields = ['State', 'partyname', 'Candidate', 'constituency_name', 'Districts', 'Residence', 'Photo',
                  'total_contested', 'no_of_votes']
'''

class statesSerializers(serializers.ModelSerializer):

    State = serializers.StringRelatedField()

    class Meta:
        model = States
        fields = ['State', 'capital', 'chief_minister', 'chief_minister_Photo', 'Governor', 'Governor_Photo']

'''
class LeadingSeatsSerializers(serializers.ModelSerializer):
    class Meta:
        model = LeadingSeats
        fields = ['MGB', 'NDA', 'LJP', 'Others']

'''
##########################################################################################

# FOR RAJYASABHA

class RajyasabhaSerializers(serializers.ModelSerializer):

    # State = serializers.StringRelatedField()
    Party = serializers.StringRelatedField()

    class Meta:
        model = Rajyasabha
        fields = ['MP_name', 'party_name', 'Party', 'gender', 'fathers_Name', 'Spouse_Name', 'Highest_Education',
                  'University', 'photo', 'address', 'elected', 'Email_address', 'Mobile']


class State_RajyasabhaSerializer(serializers.ModelSerializer):

    Rajyasabha_Candidates = RajyasabhaSerializers(many=True, read_only=True)

    class Meta:
        model = State
        fields = ['State_name', 'Rajyasabha_Candidates']

#################################################################################

# LOKSABHA


class LokSabhaSerializers(serializers.ModelSerializer):

    # State = serializers.StringRelatedField()
    Districts = serializers.StringRelatedField()
    Party = serializers.StringRelatedField()

    class Meta:
        model = LokSabha
        fields = ['Districts', 'constituency_name', 'MP_name', 'party_name', 'Party', 'gender', 'fathers_Name',
                  'Spouse_Name', 'Highest_Education', 'University', 'photo', 'address', 'Email_address', 'Mobile']


class State_loksabhaSerializer(serializers.ModelSerializer):

    Loksabha_Candidates = LokSabhaSerializers(many=True, read_only=True)

    class Meta:
        model = State
        fields = ['State_name', 'Loksabha_Candidates']

##########################################################################################################

# ASSEMBLY


class Legislative_AssemblySerializers(serializers.ModelSerializer):

    # State = serializers.StringRelatedField()
    District = serializers.StringRelatedField()
    Party = serializers.StringRelatedField()

    class Meta:
        model = Legislative_Assembly
        fields = ['District', 'constituency_name', 'MLA_name', 'party_name', 'Party', 'total_member', 'gender',
                  'fathers_Name', 'Spouse_Name', 'Highest_Education', 'University', 'photo', 'address',
                  'Email_address', 'Mobile']


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

    class Meta:
        model = Legislative_councils
        fields = ['State', 'Districts', 'constituency_name', 'MLC_name', 'elected', 'total_member', 'Email_address',
                  'Mobile']


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
        fields = ['State', 'Districts', 'Mandal', 'panchayat_name', 'Sarpanch_name', 'gender', 'fathersName',
                  'SpouseName', 'HighestEducation', 'University', 'photo', 'address', 'Email_address',
                  'Mobile']


class CorporationSerializers(serializers.ModelSerializer):

    State = serializers.StringRelatedField()
    Districts = serializers.StringRelatedField()
    City = serializers.StringRelatedField()

    class Meta:
        model = Corporation
        fields = ['State', 'Districts', 'City', 'Corporation_name', 'partyname', 'Mayor_name', 'gender', 'fathersName',
                  'SpouseName', 'HighestEducation', 'University', 'photo', 'address', 'Email_address', 'Mobile']


class Panchayat_Ward_NumberSerializers(serializers.ModelSerializer):

    State = serializers.StringRelatedField()
    Districts = serializers.StringRelatedField()

    class Meta:
        model = Panchayat_Ward_Number
        fields = ['State', 'Districts', 'Mandal', 'panchayat_name', 'Ward_Member_Name', 'gender', 'fathersName',
                  'SpouseName', 'HighestEducation', 'University', 'photo', 'address', 'Email_address', 'Mobile']


class Corporation_Ward_NumberSerializers(serializers.ModelSerializer):

    State = serializers.StringRelatedField()
    Districts = serializers.StringRelatedField()
    City = serializers.StringRelatedField()

    class Meta:
        model = Corporation_Ward_Number
        fields = ['State', 'Districts', 'City', 'Ward_name', 'partyname', 'Corporator_name', 'gender', 'fathersName',
                  'SpouseName', 'HighestEducation', 'University', 'photo', 'address', 'Email_address', 'Mobile']

######################################################################################################################

class Loksabha_SessionSerializers(serializers.ModelSerializer):

    Loksabha_MP_Name = serializers.StringRelatedField()

    class Meta:
        model = Loksabha_Session
        fields = ['Loksabha_MP_Name', 'date', 'session', 'link']

class Loksabha_Individual_SessionSerializers(serializers.ModelSerializer):

    Session_Details = Loksabha_SessionSerializers(many=True, read_only=True)

    class Meta:
        model = Parliamentary_Loksabha_Sessions
        fields = ['Session_Title', 'Session_Details']

class Loksabha_Complete_SessionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Loksabha_Complete_Session
        fields = ['Description', 'date', 'session', 'video_link']


class Complete_Loksabha_SessionSerializers(serializers.ModelSerializer):

    Loksabha_Session_Details = Loksabha_Complete_SessionSerializers(many=True, read_only=True)

    class Meta:
        model = Parliamentary_Loksabha_Sessions
        fields = ['Session_Title', 'Loksabha_Session_Details']


class Rajyasabha_Complete_SessionSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rajyasabha_Complete_Session
        fields = ['Description', 'date', 'session', 'video_link']

class Complete_Rajyasabha_SessionSerializers(serializers.ModelSerializer):

    Rajyasabha_Session_Details = Rajyasabha_Complete_SessionSerializers(many=True, read_only=True)

    class Meta:
        model = Parliamentary_Loksabha_Sessions
        fields = ['Session_Title', 'Rajyasabha_Session_Details']




#######################################################################################################################

class Rajyasabha_SessionSerializers(serializers.ModelSerializer):

    Rajyasabha = serializers.StringRelatedField()

    class Meta:
        model = Rajyasabha_Session
        fields = ['Rajyasabha', 'date', 'session', 'link']


class Rajyasabha_Individual_SessionSerializers(serializers.ModelSerializer):

    Session_Details = Rajyasabha_SessionSerializers(many=True, read_only=True)


    class Meta:
        model = Parliamentary_Rajyasabha_Sessions
        fields = ['Session_Title', 'Session_Details']

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




###########################################################################################################


class Current_Prime_MinisterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Current_Prime_Minister
        fields = ['Full_Name', 'party_name', 'Party', 'gender', 'fathers_Name', 'Spouse_Name', 'Highest_Education',
                  'University', 'Profile_photo', 'Address', 'childhood_and_Education', 'childhood_and_Education_Photo',
                  'About_Me', 'About_Me_Photo', 'aims_Goal_and_Dream', 'aims_Goal_and_Dream_Photo',
                  'Message_For_Followers', 'Email_address', 'Mobile']


class Current_PresidentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Current_President
        fields = ['Full_Name', 'gender', 'fathers_Name', 'Spouse_Name', 'Highest_Education', 'University',
                  'Profile_photo', 'Address', 'childhood_and_Education', 'childhood_and_Education_Photo',
                  'About_Me', 'About_Me_Photo', 'aims_Goal_and_Dream', 'aims_Goal_and_Dream_Photo',
                  'Message_For_Followers', 'Email_address', 'Mobile']


class Current_Vice_PresidentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Current_Vice_President
        fields = ['Full_Name', 'gender', 'fathers_Name', 'Spouse_Name', 'Highest_Education', 'University',
                  'Profile_photo', 'Address', 'childhood_and_Education', 'childhood_and_Education_Photo',
                  'About_Me', 'About_Me_Photo', 'aims_Goal_and_Dream', 'aims_Goal_and_Dream_Photo',
                  'Message_For_Followers', 'Email_address', 'Mobile']


class Current_Loksabha_SpeakerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Current_Loksabha_Speaker
        fields = ['Full_Name', 'party_name', 'Party', 'gender', 'fathers_Name', 'Spouse_Name', 'Highest_Education',
                  'University', 'Profile_photo', 'Address', 'childhood_and_Education', 'childhood_and_Education_Photo',
                  'About_Me', 'About_Me_Photo', 'Personal_Life', 'Personal_Life_Photo', 'Political_Career',
                  'Political_Career_Photo', 'aims_Goal_and_Dream', 'aims_Goal_and_Dream_Photo',
                  'Message_For_Followers', 'Email_address', 'Mobile']


class Current_Loksabha_Deputy_SpeakerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Current_Loksabha_Deputy_Speaker
        fields = ['Full_Name', 'party_name', 'Party', 'gender', 'fathers_Name', 'Spouse_Name', 'Highest_Education',
                  'University', 'Profile_photo', 'Address', 'childhood_and_Education', 'childhood_and_Education_Photo',
                  'About_Me', 'About_Me_Photo', 'Personal_Life', 'Personal_Life_Photo', 'Political_Career',
                  'Political_Career_Photo', 'aims_Goal_and_Dream', 'aims_Goal_and_Dream_Photo',
                  'Message_For_Followers', 'Email_address', 'Mobile']


class Current_Loksabha_Opposition_LeaderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Current_Loksabha_Opposition_Leader
        fields = ['Full_Name', 'party_name', 'Party', 'gender', 'fathers_Name', 'Spouse_Name', 'Highest_Education',
                  'University', 'Profile_photo', 'Address', 'childhood_and_Education', 'childhood_and_Education_Photo',
                  'About_Me', 'About_Me_Photo', 'Personal_Life', 'Personal_Life_Photo', 'Political_Career',
                  'Political_Career_Photo', 'aims_Goal_and_Dream', 'aims_Goal_and_Dream_Photo',
                  'Message_For_Followers', 'Email_address', 'Mobile']


class Current_Rajyasabha_House_LeaderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Current_Rajyasabha_House_Leader
        fields = ['Full_Name', 'party_name', 'Party', 'gender', 'fathers_Name', 'Spouse_Name', 'Highest_Education',
                  'University', 'Profile_photo', 'Address', 'childhood_and_Education', 'childhood_and_Education_Photo',
                  'About_Me', 'About_Me_Photo', 'Personal_Life', 'Personal_Life_Photo', 'Political_Career',
                  'Political_Career_Photo', 'aims_Goal_and_Dream', 'aims_Goal_and_Dream_Photo',
                  'Message_For_Followers', 'Email_address', 'Mobile']


class Current_Rajyasabha_Deputy_SpeakerSerializers(serializers.ModelSerializer):
    class Meta:
        model = Current_Rajyasabha_Deputy_Speaker
        fields = ['Full_Name', 'party_name', 'Party', 'gender', 'fathers_Name', 'Spouse_Name', 'Highest_Education',
                  'University', 'Profile_photo', 'Address', 'childhood_and_Education', 'childhood_and_Education_Photo',
                  'About_Me', 'About_Me_Photo', 'Personal_Life', 'Personal_Life_Photo', 'Political_Career',
                  'Political_Career_Photo', 'aims_Goal_and_Dream', 'aims_Goal_and_Dream_Photo',
                  'Message_For_Followers', 'Email_address', 'Mobile']


class Current_Rajyasabha_Opposition_LeaderSerializers(serializers.ModelSerializer):
    class Meta:
        model = Current_Rajyasabha_Opposition_Leader
        fields = ['Full_Name', 'party_name', 'Party', 'gender', 'fathers_Name', 'Spouse_Name', 'Highest_Education',
                  'University', 'Profile_photo', 'Address', 'childhood_and_Education', 'childhood_and_Education_Photo',
                  'About_Me', 'About_Me_Photo', 'Personal_Life', 'Personal_Life_Photo', 'Political_Career',
                  'Political_Career_Photo', 'aims_Goal_and_Dream', 'aims_Goal_and_Dream_Photo',
                  'Message_For_Followers', 'Email_address', 'Mobile']

#####################################################################################################################


class FlagSerializers(serializers.ModelSerializer):
    class Meta:
        model = Flag
        fields = ['Red1', 'Red2', 'Red3', 'White1', 'White2', 'White3', 'Green1', 'Green2', 'Green3']

################################################################################################################


class Municipal_CorporationSerializer(serializers.ModelSerializer):

    State = serializers.StringRelatedField()
    District = serializers.StringRelatedField()

    class Meta:
        model = Municipal_Corporation
        fields = ['State', 'District', 'Name']

class MayorSerializer(serializers.ModelSerializer):

    State = serializers.StringRelatedField()
    District = serializers.StringRelatedField()
    city = serializers.StringRelatedField()
    party = serializers.StringRelatedField()

    class Meta:
        model = Mayor
        fields = ['State', 'District', 'city','Municipal_Corporation_Name', 'Mayor_Name','party','areainkm2','population','formationyear','lastelectionyear']

class state_wise_MayorsSerializer(serializers.ModelSerializer):

    Corporation_Details = MayorSerializer(many=True, read_only=True)

    class Meta:
        model = State
        fields = ['State_name', 'Corporation_Details']




class CorporatorSerializer(serializers.ModelSerializer):

    State = serializers.StringRelatedField()
    District = serializers.StringRelatedField()
    Municipal_Corporation_Name = serializers.StringRelatedField()

    class Meta:
        model = Corporator
        fields = ['State', 'District', 'Municipal_Corporation_Name', 'Ward_Name', 'Corporator_Name']

class state_wise_CorporatorSerializer(serializers.ModelSerializer):

    Corporation_Name = CorporatorSerializer(many=True, read_only=True)

    class Meta:
        model = State
        fields = ['State_name', 'Corporation_Name']

class Corporation_wise_CorporatorSerializer(serializers.ModelSerializer):

    Corporation_Namees = CorporatorSerializer(many=True, read_only=True)

    class Meta:
        model = Municipal_Corporation
        fields = ['Municipal_Corporation_Name', 'Corporation_Namees']
