from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . models import Movie
from .models import BiharCandidate
from .models import DubbakaCandidate


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

         