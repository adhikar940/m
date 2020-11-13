from django.contrib.auth.models import User, Group
from rest_framework import serializers
from . models import Movie
from .models import BiharCandidate
from .models import DubbakaCandidate
from . models import BiharCandidate
from . models import DubbakaCandidate
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
from .models import UttarakhandforRajyasabha
from .models import WestBengalforRajyasabha
from .models import UttarPradeshforRajyasabha

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
from .models import Party
from rest_framework import serializers





class AndhraPradeshRajyasabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = AndhraPradeshforRajyasabha
        fields = ['MPname']

class AndhraPradeshLoksabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = AndhraPradesh
        fields = ['MPname','constituencyName']


        


class ArunachalPradeshRajyasabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = ArunachalPradeshforRajyasabha
        fields = ['MPname']

class ArunachalPradeshLoksabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = ArunachalPradesh
        fields = ['MPname','constituencyName']


        

        
class AssamRajyasabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = AssamforRajyasabha
        fields = ['MPname']

class AssamLoksabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Assam
        fields = ['MPname','constituencyName']


        
 

class BiharRajyasabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = BiharforRajyasabha
        fields = ['MPname']

class BiharLoksabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Bihar
        fields = ['MPname','constituencyName']


 

class ChhattishgarhRajyasabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChhattishgarhforRajyasabha
        fields = ['MPname']

class ChhattishgarhLoksabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Chhattishgarh
        fields = ['MPname','constituencyName']





class GoaRajyasabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = GoaforRajyasabha
        fields = ['MPname']

class GoaLoksabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Goa
        fields = ['MPname','constituencyName']




class GujaratRajyasabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = GujaratforRajyasabha
        fields = ['MPname']

class GujaratLoksabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Gujarat
        fields = ['MPname','constituencyName']





class HaryanaRajyasabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = HaryanaforRajyasabha
        fields = ['MPname']

class HaryanaLoksabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Haryana
        fields = ['MPname','constituencyName']





class HimachalPradeshRajyasabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = HimachalPradeshforRajyasabha
        fields = ['MPname']

class HimachalPradeshLoksabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = HimachalPradesh
        fields = ['MPname','constituencyName']





class JammuandKashmirRajyasabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = JammuandKashmirforRajyasabha
        fields = ['MPname']

class JammuandKashmirLoksabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = JammuandKashmir
        fields = ['MPname','constituencyName']





class JharkhandRajyasabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = JharkhandforRajyasabha
        fields = ['MPname']

class JharkhandLoksabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Jharkhand
        fields = ['MPname','constituencyName']




class KarnatakaRajyasabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = KarnatakaforRajyasabha
        fields = ['MPname']

class KarnatakaLoksabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Karnataka
        fields = ['MPname','constituencyName']




class KeralaRajyasabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = KeralaforRajyasabha
        fields = ['MPname']

class KeralaLoksabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Kerala
        fields = ['MPname','constituencyName']






class MadhyaPradeshRajyasabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = MadhyaPradeshforRajyasabha
        fields = ['MPname']

class MadhyaPradeshLoksabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = MadhyaPradesh
        fields = ['MPname','constituencyName']





class MaharashtraRajyasabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = MaharashtraforRajyasabha
        fields = ['MPname']

class MaharashtraLoksabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Maharashtra
        fields = ['MPname','constituencyName']




class ManipurRajyasabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = ManipurforRajyasabha
        fields = ['MPname']

class ManipurLoksabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Manipur
        fields = ['MPname','constituencyName']




class MeghalayaRajyasabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = MeghalayaforRajyasabha
        fields = ['MPname']

class MeghalayaLoksabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Meghalaya
        fields = ['MPname','constituencyName']




class MizoramRajyasabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = MizoramforRajyasabha
        fields = ['MPname']

class MizoramLoksabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Mizoram
        fields = ['MPname','constituencyName']





class NagalandRajyasabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = NagalandforRajyasabha
        fields = ['MPname']

class NagalandLoksabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Nagaland
        fields = ['MPname','constituencyName']





class OdishaRajyasabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = OdishaforRajyasabha
        fields = ['MPname']

class OdishaLoksabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Odisha
        fields = ['MPname','constituencyName']





class PunjabRajyasabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = PunjabforRajyasabha
        fields = ['MPname']

class PunjabLoksabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Punjab
        fields = ['MPname','constituencyName']





class RajasthanRajyasabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = RajasthanforRajyasabha
        fields = ['MPname']

class RajasthanLoksabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rajasthan
        fields = ['MPname','constituencyName']





class SikkimRajyasabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = SikkimforRajyasabha
        fields = ['MPname']

class SikkimLoksabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Sikkim
        fields = ['MPname','constituencyName']





class TamilNaduRajyasabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = TamilNaduforRajyasabha
        fields = ['MPname']

class TamilNaduLoksabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = TamilNadu
        fields = ['MPname','constituencyName']





class TelanganaRajyasabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = TelanganaforRajyasabha
        fields = ['MPname']

class TelanganaLoksabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Telangana
        fields = ['MPname','constituencyName']





class TripuraRajyasabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = TripuraforRajyasabha
        fields = ['MPname']

class TripuraLoksabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tripura
        fields = ['MPname','constituencyName']





class UttarPradeshRajyasabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = UttarPradeshforRajyasabha
        fields = ['MPname']

class UttarPradeshLoksabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = UttarPradesh
        fields = ['MPname','constituencyName']




class UttarakhandRajyasabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = UttarakhandforRajyasabha
        fields = ['MPname']

class UttarakhandLoksabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Uttarakhand
        fields = ['MPname','constituencyName']


class WestBengalRajyasabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = WestBengalforRajyasabha
        fields = ['MPname']

class WestBengalLoksabhaSerializers(serializers.ModelSerializer):
    class Meta:
        model = WestBengal
        fields = ['MPname','constituencyName']
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
        fields = ['Statename','partyname','Candidate','constituency_name','District_name','Residence','Photo','total_contested','no_of_votes']
        fields = ['Statename','partyname', 'Candidate','constituency_name', 'District_name', 'Residence', 'Photo', 'total_contested','no_of_votes']

class statesSerializers(serializers.ModelSerializer):
    class Meta:
        model = States
        fields = ['State_name', 'capital', 'chief_minister', 'chief_minister_Photo', 'Governor', 'Governor_Photo']

class LeadingSeatsSerializers(serializers.ModelSerializer):
    class Meta:
        model = LeadingSeats
        fields = ['MGB','NDA','LJP','Others']


         
        fields = ['MGB','NDA','LJP','Others']
