from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . models import Movie
from . models import BiharCandidate
from . models import DubbakaCandidate
from . models import Party
from . models import Bihar_Coalition_Party
from . models import DubbakaRunners
from . models import DubbakaWinners
from . models import BiharWinners
from . models import BiharRunners
from . models import States
from . models import LeadingSeats


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','name',]

class BiharCandidateSerializers(serializers.ModelSerializer):
    class Meta:
        model = BiharCandidate
        fields = ['Statename','partyname','Candidate','constituency_name','District_name','Residence','Photo']

class DubbakaCandidateSerializers(serializers.ModelSerializer):
    class Meta:
        model = DubbakaCandidate
        fields = ['Statename','partyname','Candidate','constituency_name','District_name','Residence','Photo']

class PartySerializers(serializers.ModelSerializer):
    class Meta:
        model = Party
        fields = ['party_status','partyname','abbreviation','President','founder','chairperson','founded_date','headquarters','seats_in_rajyasabha','seats_in_loksabha','party_symbol','founderPhoto','chairpersonPhoto']

class Bihar_Coalition_PartySerializers(serializers.ModelSerializer):
    class Meta:
        model = Bihar_Coalition_Party
        fields = ['party_status','partyname','abbreviation','President','founder','chairperson','founded_date','headquarters','seats_in_rajyasabha','seats_in_loksabha','party_symbol','founderPhoto','chairpersonPhoto']

class DubbakaRunnersSerializers(serializers.ModelSerializer):
    class Meta:
        model = DubbakaRunners
        fields = ['Statename','partyname','Candidate','constituency_name','District_name','Residence','Photo','total_contested','no_of_votes']

class DubbakaWinnersSerializers(serializers.ModelSerializer):
    class Meta:
        model = DubbakaWinners
        fields = ['Statename','partyname','Candidate','constituency_name','District_name','Residence','Photo','total_contested','no_of_votes']

class BiharWinnersSerializers(serializers.ModelSerializer):
    class Meta:
        model = BiharWinners
        fields = ['Statename','partyname','Candidate','constituency_name','District_name','Residence','Photo','total_contested','no_of_votes']

class BiharRunnersSerializers(serializers.ModelSerializer):
    class Meta:
        model = BiharRunners
        fields = ['Statename','partyname', 'Candidate','constituency_name', 'District_name', 'Residence', 'Photo', 'total_contested','no_of_votes']

class statesSerializers(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = ['State_name', 'capital', 'chief_minister', 'chief_minister_Photo', 'Governor', 'Governor_Photo']

class LeadingSeatsSerializers(serializers.ModelSerializer):
    class Meta:
        model = LeadingSeats
        fields = ['MGB','NDA','LJP','Others']