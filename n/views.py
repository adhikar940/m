from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import BiharCandidateSerializers
from .serializers import BiharRunnersSerializers
from .serializers import BiharWinnersSerializers
from .serializers import Bihar_Coalition_PartySerializers
from .serializers import DubbakaCandidateSerializers
from .serializers import DubbakaRunnersSerializers
from .serializers import DubbakaWinnersSerializers
from .serializers import LeadingSeatsSerializers
from .serializers import MovieSerializer
from .serializers import PartySerializers
from .serializers import statesSerializers
from .serializers import LokSabhaSerializers
from .serializers import RajyasabhaSerializers
from .serializers import Assembly_time_periodSerializers
from .serializers import Panchayat_time_periodSerializers
from .serializers import Municipal_corporation_time_periodSerializers
from .serializers import StateSerializers
from .serializers import DistrictsSerializers
from .serializers import CitySerializers
from .serializers import Grama_panchayatSerializers
from .serializers import CorporationSerializers
from .serializers import Panchayat_Ward_NumberSerializers
from .serializers import Corporation_Ward_NumberSerializers


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    # permission_classes = [permissions.IsAuthenticated]
    '''def list(self, request, *args, **kwargs):
        movies = Movie.objects.all()
        serializer = MovieMiniSerializer(movies, many=True)
        return Response(serializer.data)'''


class Bihar_api(APIView):
    def get(self, request):
        data = BiharCandidate.objects.all()
        serializer = BiharCandidateSerializers(data, many=True)
        return Response(serializer.data)


class Dubbaka_api(APIView):
    def get(self, request):
        data = DubbakaCandidate.objects.all()
        serializer = DubbakaCandidateSerializers(data, many=True)
        return Response(serializer.data)


class Party_api(APIView):
    def get(self, request):
        data = Party.objects.all()
        serializer = PartySerializers(data, many=True)
        return Response(serializer.data)


class Coalition_Party_api(APIView):
    def get(self, request):
        data = Bihar_Coalition_Party.objects.all()
        serializer = Bihar_Coalition_PartySerializers(data, many=True)
        return Response(serializer.data)


class BiharRunner_api(APIView):
    def get(self, request):
        data = BiharRunners.objects.all()
        serializer = BiharRunnersSerializers(data, many=True)
        return Response(serializer.data)


class BiharWinner_api(APIView):
    def get(self, request):
        data = BiharWinners.objects.all()
        serializer = BiharWinnersSerializers(data, many=True)
        return Response(serializer.data)


class DubbakaWinner_api(APIView):
    def get(self, request):
        data = DubbakaWinners.objects.all()
        serializer = DubbakaWinnersSerializers(data, many=True)
        return Response(serializer.data)


class DubbakaRunner_api(APIView):
    def get(self, request):
        data = DubbakaRunners.objects.all()
        serializer = DubbakaRunnersSerializers(data, many=True)
        return Response(serializer.data)


class Leadingseats_api(APIView):
    def get(self, request):
        data = LeadingSeats.objects.all()
        serializer = LeadingSeatsSerializers(data, many=True)
        return Response(serializer.data)


class States_api(APIView):
    def get(self, request):
        data = States.objects.all()
        serializer = statesSerializers(data, many=True)
        return Response(serializer.data)


class Rajyasabha_api(APIView):
    def get(self,request):
        data = Rajyasabha.objects.all()
        serializer = RajyasabhaSerializers(data, many=True)
        return Response(serializer.data)


class LokSabha_api(APIView):
    def get(self,request):
        data = LokSabha.objects.all()
        serializer = LokSabhaSerializers(data, many=True)
        return Response(serializer.data)


class Assembly_time_period_api(APIView):
    def get(self,request):
        data = Assembly_time_period.objects.all()
        serializer = Assembly_time_periodSerializers(data, many=True)
        return Response(serializer.data)


class Panchayat_time_period_api(APIView):
    def get(self,request):
        data = Panchayat_time_period.objects.all()
        serializer = Panchayat_time_periodSerializers(data, many=True)
        return Response(serializer.data)


class Municipal_time_period_api(APIView):
    def get(self,request):
        data = Municipal_corporation_time_period.objects.all()
        serializer = Municipal_corporation_time_periodSerializers(data, many=True)
        return Response(serializer.data)

class State_api(APIView):
    def get(self,request):
        data = State.objects.all()
        serializer = StateSerializers(data, many=True)
        return Response(serializer.data)

class Districts_api(APIView):
    def get(self,request):
        data = Districts.objects.all()
        serializer = DistrictsSerializers(data, many=True)
        return Response(serializer.data)

class City_api(APIView):
    def get(self,request):
        data = City.objects.all()
        serializer = CitySerializers(data, many=True)
        return Response(serializer.data)

class Grama_panchayat_api(APIView):
    def get(self,request):
        data = Grama_panchayat.objects.all()
        serializer = Grama_panchayatSerializers(data, many=True)
        return Response(serializer.data)

class Corporation_api(APIView):
    def get(self,request):
        data = Corporation.objects.all()
        serializer = CorporationSerializers(data, many=True)
        return Response(serializer.data)

class Panchayat_Ward_Number_api(APIView):
    def get(self,request):
        data = Panchayat_Ward_Number.objects.all()
        serializer = Panchayat_Ward_NumberSerializers(data, many=True)
        return Response(serializer.data)

class Corporation_Ward_Number_api(APIView):
    def get(self,request):
        data = Corporation_Ward_Number.objects.all()
        serializer = Corporation_Ward_NumberSerializers(data, many=True)
        return Response(serializer.data)

