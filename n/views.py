from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
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
from . serializers import MovieSerializer
from . serializers import BiharCandidateSerializers
from . serializers import DubbakaCandidateSerializers
from . serializers import PartySerializers
from . serializers import Bihar_Coalition_PartySerializers
from . serializers import DubbakaRunnersSerializers
from . serializers import DubbakaWinnersSerializers
from . serializers import BiharWinnersSerializers
from . serializers import BiharRunnersSerializers
from . serializers import statesSerializers
from . serializers import LeadingSeatsSerializers
from rest_framework.views import APIView
from rest_framework.response import Response


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    #permission_classes = [permissions.IsAuthenticated]
    '''def list(self, request, *args, **kwargs):
        movies = Movie.objects.all()
        serializer = MovieMiniSerializer(movies, many=True)
        return Response(serializer.data)'''

class Bihar_api(APIView):
    def get(self,request):
        data = BiharCandidate.objects.all()
        serializer = BiharCandidateSerializers(data, many=True)
        return Response(serializer.data)

class Dubbaka_api(APIView):
    def get(self,request):
        data = DubbakaCandidate.objects.all()
        serializer = DubbakaCandidateSerializers(data, many=True)
        return Response(serializer.data)

class Party_api(APIView):
    def get(self,request):
        data = Party.objects.all()
        serializer = PartySerializers(data, many=True)
        return Response(serializer.data)

class Coalition_Party_api(APIView):
    def get(self,request):
        data = Bihar_Coalition_Party.objects.all()
        serializer = Bihar_Coalition_PartySerializers(data, many=True)
        return Response(serializer.data)

class BiharRunner_api(APIView):
    def get(self,request):
        data = BiharRunners.objects.all()
        serializer = BiharRunnersSerializers(data, many=True)
        return Response(serializer.data)

class BiharWinner_api(APIView):
    def get(self,request):
        data = BiharWinners.objects.all()
        serializer = BiharWinnersSerializers(data, many=True)
        return Response(serializer.data)

class DubbakaWinner_api(APIView):
    def get(self,request):
        data = DubbakaWinners.objects.all()
        serializer = DubbakaWinnersSerializers(data, many=True)
        return Response(serializer.data)

class DubbakaRunner_api(APIView):
    def get(self,request):
        data = DubbakaRunners.objects.all()
        serializer = DubbakaRunnersSerializers(data, many=True)
        return Response(serializer.data)

class States_api(APIView):
    def get(self,request):
        data = States.objects.all()
        serializer = statesSerializers(data, many=True)
        return Response(serializer.data)

class Leadingseats_api(APIView):
    def get(self,request):
        data = LeadingSeats.objects.all()
        serializer = LeadingSeatsSerializers(data, many=True)
        return Response(serializer.data)
