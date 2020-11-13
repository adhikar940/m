from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from . serializers import MovieSerializer
from . serializers import BiharCandidateSerializers
from . serializers import DubbakaCandidateSerializers
from . serializers import PartySerializers
from . serializers import Bihar_Coalition_PartySerializers
from . serializers import DubbakaRunnersSerializers
from . serializers import DubbakaWinnersSerializers
from . serializers import BiharWinnersSerializers
from . serializers import BiharRunnersSerializers
from . serializers import LeadingSeatsSerializers
from . models import Movie
from . models import BiharCandidate
from . models import DubbakaCandidate
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import Party
from . models import Bihar_Coalition_Party
from . models import DubbakaRunners
from . models import DubbakaWinners
from . models import BiharWinners
from . models import BiharRunners
from . models import LeadingSeats

from .models import AndhraPradeshforRajyasabha
from .models import ArunachalPradeshforRajyasabha
from .models import AssamforRajyasabha
from .models import BiharforRajyasabha
from .models import ChhattishgarhforRajyasabha
from .models import GoaforRajyasabha
from .models import GujaratforRajyasabha
from .models import HaryanaforRajyasabha
from .models import HimachalPradeshforRajyasabha
from .models import JammuandKashmirforRajyasabha
from .models import JharkhandforRajyasabha
from .models import KarnatakaforRajyasabha
from .models import KeralaforRajyasabha
from .models import MadhyaPradeshforRajyasabha
from .models import MaharashtraforRajyasabha
from .models import ManipurforRajyasabha
from .models import MeghalayaforRajyasabha
from .models import MizoramforRajyasabha
from .models import NagalandforRajyasabha
from .models import OdishaforRajyasabha
from .models import PunjabforRajyasabha
from .models import RajasthanforRajyasabha
from .models import SikkimforRajyasabha
from .models import TamilNaduforRajyasabha
from .models import TelanganaforRajyasabha
from .models import TripuraforRajyasabha
from .models import UttarPradeshforRajyasabha
from .models import UttarakhandforRajyasabha
from .models import WestBengalforRajyasabha

from .models import AndhraPradesh
from .models import ArunachalPradesh
from .models import Assam
from .models import Bihar
from .models import Chhattishgarh
from .models import Goa
from .models import Gujarat
from .models import Haryana
from .models import HimachalPradesh
from .models import JammuandKashmir
from .models import Jharkhand
from .models import Karnataka
from .models import Kerala
from .models import MadhyaPradesh
from .models import Maharashtra
from .models import Manipur
from .models import Meghalaya
from .models import Mizoram
from .models import Nagaland
from .models import Odisha
from .models import Punjab
from .models import Rajasthan
from .models import Sikkim
from .models import TamilNadu
from .models import Telangana
from .models import Tripura
from .models import Uttarakhand
from .models import WestBengal
from .models import UttarPradesh

from .serializers import AndhraPradeshRajyasabhaSerializers
from .serializers import ArunachalPradeshRajyasabhaSerializers
from .serializers import AssamRajyasabhaSerializers
from .serializers import BiharRajyasabhaSerializers
from .serializers import ChhattishgarhRajyasabhaSerializers
from .serializers import GoaRajyasabhaSerializers
from .serializers import GujaratRajyasabhaSerializers
from .serializers import HaryanaRajyasabhaSerializers
from .serializers import HimachalPradeshRajyasabhaSerializers
from .serializers import JammuandKashmirRajyasabhaSerializers
from .serializers import JharkhandRajyasabhaSerializers
from .serializers import KarnatakaRajyasabhaSerializers
from .serializers import KeralaRajyasabhaSerializers
from .serializers import MadhyaPradeshRajyasabhaSerializers
from .serializers import MaharashtraRajyasabhaSerializers
from .serializers import ManipurRajyasabhaSerializers
from .serializers import MeghalayaRajyasabhaSerializers
from .serializers import MizoramRajyasabhaSerializers
from .serializers import NagalandRajyasabhaSerializers
from .serializers import OdishaRajyasabhaSerializers
from .serializers import PunjabRajyasabhaSerializers
from .serializers import RajasthanRajyasabhaSerializers
from .serializers import SikkimRajyasabhaSerializers
from .serializers import TamilNaduRajyasabhaSerializers
from .serializers import TelanganaRajyasabhaSerializers
from .serializers import TripuraRajyasabhaSerializers
from .serializers import UttarPradeshRajyasabhaSerializers
from .serializers import UttarakhandRajyasabhaSerializers
from .serializers import WestBengalRajyasabhaSerializers


from .serializers import AndhraPradeshLoksabhaSerializers
from .serializers import ArunachalPradeshLoksabhaSerializers
from .serializers import AssamLoksabhaSerializers
from .serializers import BiharLoksabhaSerializers
from .serializers import ChhattishgarhLoksabhaSerializers
from .serializers import GoaLoksabhaSerializers
from .serializers import GujaratLoksabhaSerializers
from .serializers import HaryanaLoksabhaSerializers
from .serializers import HimachalPradeshLoksabhaSerializers
from .serializers import JammuandKashmirLoksabhaSerializers
from .serializers import JharkhandLoksabhaSerializers
from .serializers import KarnatakaLoksabhaSerializers
from .serializers import KeralaLoksabhaSerializers
from .serializers import MadhyaPradeshLoksabhaSerializers
from .serializers import MaharashtraLoksabhaSerializers
from .serializers import ManipurLoksabhaSerializers
from .serializers import MeghalayaLoksabhaSerializers
from .serializers import MizoramLoksabhaSerializers
from .serializers import NagalandLoksabhaSerializers
from .serializers import OdishaLoksabhaSerializers
from .serializers import PunjabLoksabhaSerializers
from .serializers import RajasthanLoksabhaSerializers
from .serializers import SikkimLoksabhaSerializers
from .serializers import TamilNaduLoksabhaSerializers
from .serializers import TelanganaLoksabhaSerializers
from .serializers import TripuraLoksabhaSerializers
from .serializers import UttarPradeshLoksabhaSerializers
from .serializers import UttarakhandLoksabhaSerializers
from .serializers import WestBengalLoksabhaSerializers




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

class Leadingseats_api(APIView):
    def get(self,request):
        data = LeadingSeats.objects.all()
        serializer = LeadingSeatsSerializers(data, many=True)
        return Response(serializer.data)


class AndhraPradeshrajyasabha_api(APIView):
    def get(self,request):
        data = AndhraPradeshforRajyasabha.objects.all()
        serializer = AndhraPradeshRajyasabhaSerializers(data, many=True)
        return Response(serializer.data)

class AndhraPradeshloksabha_api(APIView):
    def get(self,request):
        data = AndhraPradesh.objects.all()
        serializer = AndhraPradeshLoksabhaSerializers(data, many=True)
        return Response(serializer.data)



class ArunachalPradeshrajyasabha_api(APIView):
    def get(self,request):
        data = ArunachalPradeshforRajyasabha.objects.all()
        serializer = ArunachalPradeshRajyasabhaSerializers(data, many=True)
        return Response(serializer.data)

class ArunachalPradeshloksabha_api(APIView):
    def get(self,request):
        data = ArunachalPradesh.objects.all()
        serializer = ArunachalPradeshLoksabhaSerializers(data, many=True)
        return Response(serializer.data)



class Assamrajyasabha_api(APIView):
    def get(self,request):
        data = AssamforRajyasabha.objects.all()
        serializer = AssamRajyasabhaSerializers(data, many=True)
        return Response(serializer.data)

class Assamloksabha_api(APIView):
    def get(self,request):
        data = Assam.objects.all()
        serializer = AssamLoksabhaSerializers(data, many=True)
        return Response(serializer.data)



class Biharrajyasabha_api(APIView):
    def get(self,request):
        data = BiharforRajyasabha.objects.all()
        serializer = BiharRajyasabhaSerializers(data, many=True)
        return Response(serializer.data)

class Biharloksabha_api(APIView):
    def get(self,request):
        data = Bihar.objects.all()
        serializer = BiharLoksabhaSerializers(data, many=True)
        return Response(serializer.data)




class Chhattishgarhrajyasabha_api(APIView):
    def get(self,request):
        data = ChhattishgarhforRajyasabha.objects.all()
        serializer = ChhattishgarhRajyasabhaSerializers(data, many=True)
        return Response(serializer.data)

class Chhattishgarhloksabha_api(APIView):
    def get(self,request):
        data = Chhattishgarh.objects.all()
        serializer = ChhattishgarhLoksabhaSerializers(data, many=True)
        return Response(serializer.data)




class Goarajyasabha_api(APIView):
    def get(self,request):
        data = GoaforRajyasabha.objects.all()
        serializer = GoaRajyasabhaSerializers(data, many=True)
        return Response(serializer.data)

class Goaloksabha_api(APIView):
    def get(self,request):
        data = Goa.objects.all()
        serializer = GoaLoksabhaSerializers(data, many=True)
        return Response(serializer.data)




class Gujaratrajyasabha_api(APIView):
    def get(self,request):
        data = GujaratforRajyasabha.objects.all()
        serializer = GujaratRajyasabhaSerializers(data, many=True)
        return Response(serializer.data)

class Gujaratloksabha_api(APIView):
    def get(self,request):
        data = Gujarat.objects.all()
        serializer = GujaratLoksabhaSerializers(data, many=True)
        return Response(serializer.data)




class Haryanarajyasabha_api(APIView):
    def get(self,request):
        data = HaryanaforRajyasabha.objects.all()
        serializer = HaryanaRajyasabhaSerializers(data, many=True)
        return Response(serializer.data)

class Haryanaloksabha_api(APIView):
    def get(self,request):
        data = Haryana.objects.all()
        serializer = HaryanaLoksabhaSerializers(data, many=True)
        return Response(serializer.data)



class HimachalPradeshrajyasabha_api(APIView):
    def get(self,request):
        data = HimachalPradeshforRajyasabha.objects.all()
        serializer = HimachalPradeshRajyasabhaSerializers(data, many=True)
        return Response(serializer.data)

class HimachalPradeshloksabha_api(APIView):
    def get(self,request):
        data = HimachalPradesh.objects.all()
        serializer = HimachalPradeshLoksabhaSerializers(data, many=True)
        return Response(serializer.data)



class JammuandKashmirrajyasabha_api(APIView):
    def get(self,request):
        data = JammuandKashmirforRajyasabha.objects.all()
        serializer = JammuandKashmirRajyasabhaSerializers(data, many=True)
        return Response(serializer.data)

class JammuandKashmirloksabha_api(APIView):
    def get(self,request):
        data = JammuandKashmir.objects.all()
        serializer = JammuandKashmirLoksabhaSerializers(data, many=True)
        return Response(serializer.data)




class Jharkhandrajyasabha_api(APIView):
    def get(self,request):
        data = JharkhandforRajyasabha.objects.all()
        serializer = JharkhandRajyasabhaSerializers(data, many=True)
        return Response(serializer.data)

class Jharkhandloksabha_api(APIView):
    def get(self,request):
        data = Jharkhand.objects.all()
        serializer = JharkhandLoksabhaSerializers(data, many=True)
        return Response(serializer.data)




class Karnatakarajyasabha_api(APIView):
    def get(self,request):
        data = KarnatakaforRajyasabha.objects.all()
        serializer = KarnatakaRajyasabhaSerializers(data, many=True)
        return Response(serializer.data)

class Karnatakaloksabha_api(APIView):
    def get(self,request):
        data = Karnataka.objects.all()
        serializer = KarnatakaLoksabhaSerializers(data, many=True)
        return Response(serializer.data)


class Keralarajyasabha_api(APIView):
    def get(self,request):
        data = KeralaforRajyasabha.objects.all()
        serializer = KeralaRajyasabhaSerializers(data, many=True)
        return Response(serializer.data)

class Keralaloksabha_api(APIView):
    def get(self,request):
        data = Kerala.objects.all()
        serializer = KeralaLoksabhaSerializers(data, many=True)
        return Response(serializer.data)



class MadhyaPradeshrajyasabha_api(APIView):
    def get(self,request):
        data = MadhyaPradeshforRajyasabha.objects.all()
        serializer = MadhyaPradeshRajyasabhaSerializers(data, many=True)
        return Response(serializer.data)

class MadhyaPradeshloksabha_api(APIView):
    def get(self,request):
        data = MadhyaPradesh.objects.all()
        serializer = MadhyaPradeshLoksabhaSerializers(data, many=True)
        return Response(serializer.data)




class Maharashtrarajyasabha_api(APIView):
    def get(self,request):
        data = MaharashtraforRajyasabha.objects.all()
        serializer = MaharashtraRajyasabhaSerializers(data, many=True)
        return Response(serializer.data)

class Maharashtraloksabha_api(APIView):
    def get(self,request):
        data = Maharashtra.objects.all()
        serializer = MaharashtraLoksabhaSerializers(data, many=True)
        return Response(serializer.data)




class Manipurrajyasabha_api(APIView):
    def get(self,request):
        data = ManipurforRajyasabha.objects.all()
        serializer = ManipurRajyasabhaSerializers(data, many=True)
        return Response(serializer.data)

class Manipurloksabha_api(APIView):
    def get(self,request):
        data = Manipur.objects.all()
        serializer = ManipurLoksabhaSerializers(data, many=True)
        return Response(serializer.data)




class Meghalayarajyasabha_api(APIView):
    def get(self,request):
        data = MeghalayaforRajyasabha.objects.all()
        serializer = MeghalayaRajyasabhaSerializers(data, many=True)
        return Response(serializer.data)

class Meghalayaloksabha_api(APIView):
    def get(self,request):
        data = Meghalaya.objects.all()
        serializer = MeghalayaLoksabhaSerializers(data, many=True)
        return Response(serializer.data)




class Mizoramrajyasabha_api(APIView):
    def get(self,request):
        data = MizoramforRajyasabha.objects.all()
        serializer = MizoramRajyasabhaSerializers(data, many=True)
        return Response(serializer.data)

class Mizoramloksabha_api(APIView):
    def get(self,request):
        data = Mizoram.objects.all()
        serializer = MizoramLoksabhaSerializers(data, many=True)
        return Response(serializer.data)




class Nagalandrajyasabha_api(APIView):
    def get(self,request):
        data = NagalandforRajyasabha.objects.all()
        serializer = NagalandRajyasabhaSerializers(data, many=True)
        return Response(serializer.data)

class Nagalandloksabha_api(APIView):
    def get(self,request):
        data = Nagaland.objects.all()
        serializer = NagalandLoksabhaSerializers(data, many=True)
        return Response(serializer.data)



class Odisharajyasabha_api(APIView):
    def get(self,request):
        data = OdishaforRajyasabha.objects.all()
        serializer = OdishaRajyasabhaSerializers(data, many=True)
        return Response(serializer.data)

class Odishaloksabha_api(APIView):
    def get(self,request):
        data = Odisha.objects.all()
        serializer = OdishaLoksabhaSerializers(data, many=True)
        return Response(serializer.data)



class Punjabrajyasabha_api(APIView):
    def get(self,request):
        data = PunjabforRajyasabha.objects.all()
        serializer = PunjabRajyasabhaSerializers(data, many=True)
        return Response(serializer.data)

class Punjabloksabha_api(APIView):
    def get(self,request):
        data = Punjab.objects.all()
        serializer = PunjabLoksabhaSerializers(data, many=True)
        return Response(serializer.data)




class Rajasthanrajyasabha_api(APIView):
    def get(self,request):
        data = RajasthanforRajyasabha.objects.all()
        serializer = RajasthanRajyasabhaSerializers(data, many=True)
        return Response(serializer.data)

class Rajasthanloksabha_api(APIView):
    def get(self,request):
        data = Rajasthan.objects.all()
        serializer = RajasthanLoksabhaSerializers(data, many=True)
        return Response(serializer.data)





class Sikkimrajyasabha_api(APIView):
    def get(self,request):
        data = SikkimforRajyasabha.objects.all()
        serializer = SikkimRajyasabhaSerializers(data, many=True)
        return Response(serializer.data)

class Sikkimloksabha_api(APIView):
    def get(self,request):
        data = Sikkim.objects.all()
        serializer = SikkimLoksabhaSerializers(data, many=True)
        return Response(serializer.data)




class TamilNadurajyasabha_api(APIView):
    def get(self,request):
        data = TamilNaduforRajyasabha.objects.all()
        serializer = TamilNaduRajyasabhaSerializers(data, many=True)
        return Response(serializer.data)

class TamilNaduloksabha_api(APIView):
    def get(self,request):
        data = TamilNadu.objects.all()
        serializer = TamilNaduLoksabhaSerializers(data, many=True)
        return Response(serializer.data)




class Telanganarajyasabha_api(APIView):
    def get(self,request):
        data = TelanganaforRajyasabha.objects.all()
        serializer = TelanganaRajyasabhaSerializers(data, many=True)
        return Response(serializer.data)

class Telanganaloksabha_api(APIView):
    def get(self,request):
        data = Telangana.objects.all()
        serializer = TelanganaLoksabhaSerializers(data, many=True)
        return Response(serializer.data)




class Tripurarajyasabha_api(APIView):
    def get(self,request):
        data = TripuraforRajyasabha.objects.all()
        serializer = TripuraRajyasabhaSerializers(data, many=True)
        return Response(serializer.data)

class Tripuraloksabha_api(APIView):
    def get(self,request):
        data = Tripura.objects.all()
        serializer = TripuraLoksabhaSerializers(data, many=True)
        return Response(serializer.data)




class UttarPradeshrajyasabha_api(APIView):
    def get(self,request):
        data = UttarPradeshforRajyasabha.objects.all()
        serializer = UttarPradeshRajyasabhaSerializers(data, many=True)
        return Response(serializer.data)

class UttarPradeshloksabha_api(APIView):
    def get(self,request):
        data = UttarPradesh.objects.all()
        serializer = UttarPradeshLoksabhaSerializers(data, many=True)
        return Response(serializer.data)




class Uttarakhandrajyasabha_api(APIView):
    def get(self,request):
        data = UttarakhandforRajyasabha.objects.all()
        serializer = UttarakhandRajyasabhaSerializers(data, many=True)
        return Response(serializer.data)

class Uttarakhandloksabha_api(APIView):
    def get(self,request):
        data = Uttarakhand.objects.all()
        serializer = UttarakhandLoksabhaSerializers(data, many=True)
        return Response(serializer.data)




class WestBengalrajyasabha_api(APIView):
    def get(self,request):
        data = WestBengalforRajyasabha.objects.all()
        serializer = WestBengalRajyasabhaSerializers(data, many=True)
        return Response(serializer.data)

class WestBengalloksabha_api(APIView):
    def get(self,request):
        data = WestBengal.objects.all()
        serializer = WestBengalLoksabhaSerializers(data, many=True)
        return Response(serializer.data)




