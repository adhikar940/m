from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
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
from .serializers import Legislative_AssemblySerializers
from .serializers import Legislative_CouncilSerializers
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
from .serializers import CarsSerializer

from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import SignupForm, User_infoForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *


# sign_up view function

def sign_up(request):
    if request.method == "POST":
        fm = SignupForm(request.POST)

        if fm.is_valid():
            messages.success(request, 'Account Created Successfully..!')
            fm.save()

    else:
        fm = SignupForm()
    return render(request, 'n/Signup.html', {'form': fm})


# Login view form

def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":

            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                username = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    messages.success(request, 'Account loggedin Successfully..!')
                    return HttpResponseRedirect('/profile/')

        else:
            fm = AuthenticationForm()
        return render(request, 'n/userlogin.html', {'form': fm})
    else:
        return HttpResponseRedirect('/profile/')

def party_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":

            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                username = fm.cleaned_data['username']
                password = fm.cleaned_data['password']
                user = authenticate(username=username, password=password)

                if user is not None:
                    login(request, user)
                    messages.success(request, 'Account loggedin Successfully..!')
                    return HttpResponseRedirect('/partyprofile/')

        else:
            fm = AuthenticationForm()
        return render(request, 'n/partylogin.html', {'form': fm})
    else:
        return HttpResponseRedirect('/partyprofile/')

# home profile

@login_required
def profile(request):

    logged_user = request.user
    form = user_profile.objects.filter(user=logged_user)
    context = {'form': form}
    return render(request, 'n/profile.html', context)

@login_required
def partyprofile(request):
    #if authenticate(username='BJP',password='Bjp@1234'):
     #   posts = Rajyasabha.objects.filter(Party = 'BJP')
        return render(request, 'n/partyprofile.html')

    #logged_user = request.user
    #party = logged_user
    #form = Rajyasabha.objects.filter(Party=party)
    #context = {'form': form}

# USER INFO

                 
def model_form_upload(request):
    if request.user.is_authenticated:
        user = request.user
        if request.method == 'POST':
            form = User_infoForm(request.POST, request.FILES)
            if form.is_valid():
                childhood_and_Education = form.cleaned_data.get('childhood_and_Education_Photo')
                childhood_and_Education_Photo = form.cleaned_data.get('childhood_and_Education_Photo')
                About_Me = form.cleaned_data.get('About_Me')
                About_Me_Photo = form.cleaned_data.get('About_Me_Photo')
                Personal_Life = form.cleaned_data.get('Personal_Life')
                Personal_Life_Photo = form.cleaned_data.get('Personal_Life_Photo')
                Political_Career = form.cleaned_data.get('Political_Career')
                Political_Career_Photo = form.cleaned_data.get('Political_Career_Photo')
                aims_Goal_and_Dream = form.cleaned_data.get('aims_Goal_and_Dream')
                aims_Goal_and_Dream_Photo = form.cleaned_data.get('aims_Goal_and_Dream_Photo')
                Message_For_Followers = form.cleaned_data.get('Message_For_Followers')
                Photo = form.cleaned_data.get('Photo')
                user_profile.objects.create(
                    user = user,
                    childhood_and_Education = childhood_and_Education,
                    childhood_and_Education_Photo = childhood_and_Education_Photo,
                    About_Me = About_Me,
                    About_Me_Photo =About_Me_Photo,
                    Personal_Life = Personal_Life,
                    Personal_Life_Photo = Personal_Life_Photo,
                    Political_Career = Political_Career,
                    Political_Career_Photo =Political_Career_Photo,
                    aims_Goal_and_Dream = aims_Goal_and_Dream,
                    aims_Goal_and_Dream_Photo = aims_Goal_and_Dream_Photo,
                    Message_For_Followers = Message_For_Followers,
                    Photo = Photo,
                )
                return redirect('profile')
        else:
            form = User_infoForm()
        return render(request, 'n/Post_user_info.html', {'form': form})


def user_info(request):

    instance = user_profile(user=request.user)
    form = User_infoForm(instance=instance)
    if request.method == 'POST':
        form = User_infoForm(request.POST)
        if form.is_valid():
            return redirect('profile')

    context = {'form': form}
    return render(request, "n/Post_user_info.html", context)


# TO UPDATE THE USER_INFO

@login_required
def update_user_info(request):
    if request.method  == 'POST':
        form = User_infoForm(request.POST, request.FILES, instance=request.user.user_profile)
        if form.is_valid():
            model_instance = form.save()
            model_instance.user=request.user
            model_instance.childhood_and_Education = form.cleaned_data.get('childhood_and_Education')
            model_instance.childhood_and_Education_Photo = form.cleaned_data.get('childhood_and_Education_Photo')
            model_instance.About_Me = form.cleaned_data.get('About_Me')
            model_instance.About_Me_Photo = form.cleaned_data.get('About_Me_Photo')
            model_instance.Personal_Life = form.cleaned_data.get('Personal_Life')
            model_instance.Personal_Life_Photo = form.cleaned_data.get('Personal_Life_Photo')
            model_instance.Political_Career = form.cleaned_data.get('Political_Career')
            model_instance.Political_Career_Photo = form.cleaned_data.get('Political_Career_Photo')
            model_instance.aims_Goal_and_Dream = form.cleaned_data.get('aims_Goal_and_Dream')
            model_instance.aims_Goal_and_Dream_Photo = form.cleaned_data.get('aims_Goal_and_Dream_Photo')
            model_instance.Message_For_Followers = form.cleaned_data.get('Message_For_Followers')
            model_instance.Photo = form.cleaned_data.get('Photo')
            
            model_instance.save()
            return redirect('profile')
    else:
         form = User_infoForm(instance=request.user.user_profile)
    return render(request, 'n/update_user_info.html', {'form': form})


# logout
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

def party_logout(request):
    logout(request)
    return HttpResponseRedirect('/partylogin/')


# Change Password using old Password

def user_change_password(request):

    if request.user.is_authenticated:
        if request.method == "POST":

            fm = PasswordChangeForm(user=request.user, data=request.POST)
            if fm.is_valid():
                fm.save()
                return HttpResponseRedirect('/login/')
        else:
            fm = PasswordChangeForm(user=request.user)
        return render(request, 'n/changepassword.html', {'form': fm})
    else:
        return HttpResponseRedirect('/login/')


# Forgot Password..
def user_forgot_password(request):
    return HttpResponseRedirect('/reset_password/')





class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    #permission_classes = [permissions.IsAuthenticated]
    


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

class CarsAPIView(viewsets.ModelViewSet):
    serializer_class = CarsSerializer
    
    def get_queryset(self):
        cars_specs = Rajyasabha.objects.all()
        return cars_specs

    def retrieve(self, request, *args, **kwargs):
        params = kwargs
        print(params['pk'])
        cars = Rajyasabha.objects.filter(id = params['pk'])
        serializer = CarsSerializer(cars, many = True)

        return Response((serializer.data))

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


class Assembly_api(APIView):
    def get(self,request):
        data = Legislative_Assembly.objects.all()
        serializer = Legislative_AssemblySerializers(data, many=True)
        return Response(serializer.data)

class Legislative_Council_api(APIView):
    def get(self,request):
        data = Legislative_Council.objects.all()
        serializer = Legislative_CouncilSerializers(data, many=True)
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

class Loksabha_Session_api(APIView):
    def get(self,request):
        data = Loksabha_Session.objects.all()
        serializer = Loksabha_SessionSerializers(data, many=True)
        return Response(serializer.data)

class Rajyasabha_Session_api(APIView):
    def get(self,request):
        data = Rajyasabha_Session.objects.all()
        serializer = Rajyasabha_SessionSerializers(data, many=True)
        return Response(serializer.data)

class Legislative_Assembly_Session_api(APIView):
    def get(self,request):
        data = Legislative_Assembly_Session.objects.all()
        serializer = Legislative_Assembly_SessionSerializers(data, many=True)
        return Response(serializer.data)

class Legislative_counsil_Session_api(APIView):
    def get(self,request):
        data = Legislative_counsil_Session.objects.all()
        serializer = Legislative_counsil_SessionSerializers(data, many=True)
        return Response(serializer.data)


