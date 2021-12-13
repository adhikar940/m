from rest_framework import viewsets,status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
from django.shortcuts import render, HttpResponseRedirect, redirect
from .forms import User_infoForm, PasswordForm
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .serializers import *
from django.core.mail import send_mail
from django.conf import settings
import random
import string
from passlib.hash import pbkdf2_sha256
from django.contrib.auth.models import User
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import action
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User
from .serializers import ChangePasswordSerializer
from validate_email import validate_email
from RandomWordGenerator import RandomWord
import re
from django.core.mail import send_mail
from .decorators import *
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import Group
from rest_framework.decorators import api_view
from . import kkkk
from rest_framework.authtoken.views import ObtainAuthToken
from django.http import HttpResponse
mnf = "adhikar869@gmail.com"
regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
'''class LlViewSet(ModelViewSet):
    queryset = LokSabha.objects.all()
    serializer_class = LlSerializer
    permission_classes = [AllowAny]'''
from rest_framework.permissions import BasePermission
class PartyView(generics.ListAPIView):
    queryset = Party.objects.all()
    serializer_class = PartySerializers
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields = ('partyname', 'abbreviation', )
    search_fields = ('partyname', 'abbreviation', )
class AssemblyconstituencyView(generics.ListAPIView):
    queryset = Assembly_Constituency.objects.all()
    serializer_class = Assembly_ConstituencySerializers
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields = ('Assembly_Constituency_Name',)
    search_fields = ('Assembly_Constituency_Name', )
def tmail(request):
    print(kkkk.em)
    send_mail(
        # title:
        "Account",
        # message:
        "Email Working",
        # from:
        kkkk.em,
        # to:
        [kkkk.e,]
    )
    return HttpResponse("Mail Sent")
class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        response = super(CustomObtainAuthToken, self).post(request, *args, **kwargs)
        token = Token.objects.get(key=response.data['token'])
        user = User.objects.get(id=token.user_id)
        mnf=user.first_name
        userSerilizer = UserSerializer(user, many=False)
        #userSerilizer.data
        return Response({'token': token.key, 'mn':mnf })
class IsGroupUser(BasePermission):
    group = None
    def has_permission(self, request, view):
        user = request.user
        return user.is_authenticated and user.groups.filter(name=self.group).exists()
class Isparty(IsGroupUser):
    group = 'party'
class Isadmin(IsGroupUser):
    group = 'admin'
class IsloksabhaMP(IsGroupUser):
    group = 'loksabhaMP'
class IsrajyasabhaMP(IsGroupUser):
    group = 'rajyasabhaMP'
class Ismla(IsGroupUser):
    group = 'mla'
class Ismlc(IsGroupUser):
    group = 'mlc'

def check(email):
    # pass the regular expression
    # and the string in search() method
    if(re.search(regex, email)):
        print("Valid Email")

    else:
        print("Invalid Email")
#from django.core.validators import email_re

class ChangePasswordView(generics.UpdateAPIView):
    """
    An endpoint for changing password.
    """
    serializer_class = ChangePasswordSerializer
    model = User
    permission_classes = (IsAuthenticated,)

    def get_object(self, queryset=None):
        obj = self.request.user
        return obj

    def update(self, request, *args, **kwargs):
        self.object = self.get_object()
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            # Check old password
            if not self.object.check_password(serializer.data.get("old_password")):
                return Response({"old_password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
            # set_password also hashes the password that the user will get
            self.object.set_password(serializer.data.get("new_password"))
            self.object.save()
            response = {
                'status': 'success',
                'code': status.HTTP_200_OK,
                'message': 'Password updated successfully',
                'data': []
            }
            return Response(response)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
class statepartyapi(APIView):
    permission_classes = (Isparty,)
    authentication_classes = (TokenAuthentication, )
    def post(self, request):
        if 'email' in request.data:
            e = request.data['email']
            g=request.data['id']
            f=request.data['state']
            party=Party.objects.get(id=g)
            S = State.objects.get(id=f)
            s1=S.State_name
            e=e.lower()
            p = party.abbreviation
            p1=party.partyname
            if User.objects.filter(email=e).exists():
                response = {'m':'This email already exists'}
                return Response(response, status=status.HTTP_200_OK)
            else :
                r=RandomWord(max_word_size=10,
                constant_word_size=True,
                include_digits=True,
                special_chars=r"@_!#$%^&*()<>?/\|}{~:",
                include_special_chars=False)
                passw=r.generate()
                if(party.stateactivated == 'no'):
                    party.stateactivated = f
                    party.save()
                else :
                    zmn = party.stateactivated
                    zm = zmn.split('-')
                    zmnp = 0
                    while(zmnp < len(zm)):
                        if(zm[zmnp] == f):
                            response = {'m':'Account already created for this state'}
                            return Response(response, status=status.HTTP_200_OK)
                        zmnp = zmnp+1
                    party.stateactivated = zmn+'-'+f
                    party.save()
                send_mail(
                    # title:
                    "Account created for {title}".format(title="www.adhikar.net"),
                    # message:
                    "Welcome to India's first political social networking site. Thank you for creating the party {pp}'s account for the state {ss} with www.adhikar.net. You can login with the credentials username - {u} and password - {p}".format(pp=p,ss=s1, u=e,p=passw),
                    # from:
                    kkkk.em,
                    # to:
                    [e,kkkk.em1]
                )
                q="sparty-"+p+"-"+g+"-"+f
                user =User(email=e,first_name=q,last_name=f+'-'+p1,username=e)
                user.set_password(passw)
                user.save()
                new_group = Group.objects.get(name = 'party')
                user = User.objects.get(username = e)
                user.groups.add(new_group)
                response = {'m':'Account created'}
                return Response(response, status=status.HTTP_200_OK)
        else :
            response = {'m':'Kindly provide a valid email'}
            return Response(response, status=status.HTTP_200_OK)
class PartyViewSet(viewsets.ModelViewSet):
    queryset = Party.objects.all()
    serializer_class = PSerializers
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsAdminUser, )
    @action(detail=True, methods=['POST'])
    def k(self,request,pk=None):
        if 'email' in request.data:
            e = request.data['email']
            is_valid = validate_email(e)
            is_valid = True
            party=Party.objects.get(id=pk)
            if(party.actvated == 'yes'):
                response = {'m':'Account already activated'}
                return Response(response, status=status.HTTP_200_OK)
            elif(is_valid == True or None):
                e=e.lower()
                p = party.abbreviation
                p1=party.partyname
                if User.objects.filter(email=e).exists():
                    response = {'m':'This email already exists'}
                    return Response(response, status=status.HTTP_200_OK)
                else :
                    r=RandomWord(max_word_size=10,
                    constant_word_size=True,
                    include_digits=True,
                    special_chars=r"@_!#$%^&*()<>?/\|}{~:",
                    include_special_chars=False)
                    passw=r.generate()
                    send_mail(
                        # title:
                        "Account created for {title}".format(title="www.adhikar.net"),
                        # message:
                        "Welcome for India's first political social networking site. Thank you for creating the party {pp}'s account with www.adhikar.net. You can login with the credentials username - {u} and password - {p}".format(pp=p, u=e,p=passw),
                        # from:
                        kkkk.em,
                        # to:
                        [e,kkkk.em1]
                    )
                    q="party-"+p+"-"+pk
                    user =User(email=e,first_name=q,last_name=p1,username=e)
                    user.set_password(passw)
                    user.save()
                    new_group = Group.objects.get(name = 'party')
                    user = User.objects.get(username = e)
                    user.groups.add(new_group)
                    party.actvated = 'yes'
                    party.save()
                    response = {'m':'Account created'}
                    return Response(response, status=status.HTTP_200_OK)
                    '''try:
                        kk=send_mail(
                            # title:
                            "Account created for {title}".format(title="www.adhikar.net"),
                            # message:
                            "Congratulations, your account on www.adhikar.net is activated. You can login with the credentials username - {u} and password - {p}".format(u=e,p=passw),
                            # from:
                            config.EMAIL_ADDRESS,
                            # to:
                            [e,]
                        )
                        if(kk==1):
                            q="party-"+p
                            user =User(email=e,first_name=q,last_name=p1,username=e)
                            user.set_password(passw)
                            user.save()
                            new_group = Group.objects.get(name = 'party')
                            print(type(new_group))       # return <class 'django.contrib.auth.models.Group'>
                            user = User.objects.get(username = e)
                            user.groups.add(new_group)
                            party.actvated = 'yes'
                            party.save()
                            response = {'m':'Account created'}
                        else :
                            response = {'m':'Failed to deliver the mail, Hemce the account not created. This may due to invalid email. Kindly provide a Valid email'}
                        return Response(response, status=status.HTTP_200_OK)
                    except :
                        response = {'m':'Failed to deliver the mail, Hemce the account not created. This may due to invalid email. Kindly provide a Valid email'}
                        return Response(response, status=status.HTTP_200_OK)'''
            else :
                response = {'m':'Kindly provide a valid email'}
                return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'m':'Kindly provide the mail'}
            return Response(response, status=status.HTTP_200_OK)

class Party_api(APIView):
    def get(self, request):
        data = Party.objects.all()
        serializer = PartySerializers(data, many=True)
        return Response(serializer.data)
class Activatedparty(APIView):
    def get(self, request):
        data = Party.objects.all().filter(actvated ='yes')
        serializer = PartySerializers(data, many=True)
        return Response(serializer.data)
class Coalition_Party_api(APIView):
    def get(self, request):
        data = Bihar_Coalition_Party.objects.all()
        serializer = Bihar_Coalition_PartySerializers(data, many=True)
        return Response(serializer.data)
class State_api(APIView):
    def get(self, request):
        data = State.objects.all()
        serializer = stateSerializers(data, many=True)
        return Response(serializer.data)

class States_api(APIView):
    def get(self, request):
        data = States.objects.all()
        serializer = statesSerializers(data, many=True)
        return Response(serializer.data)



##################################     Rajya Sabha    ##################################################
class Rajyasabha_Members_api(APIView):
    def get(self,request):
        data = Rajyasabha.objects.all()
        serializer = RajyasabhaSerializers(data, many=True)
        return Response(serializer.data)
class Rajyasabhapresedent(APIView):
    def get(self,request):
        data = Rajyasabhapresedential.objects.all()
        serializer = RajyasabhapresedentialSerializers(data, many=True)
        return Response(serializer.data)
class State_Wise_Rajyasabha_Candidates_api(APIView):
    def get(self, request):
        data = State.objects.all()
        serializer = State_RajyasabhaSerializer(data, many=True)
        return Response(serializer.data)
class stateWise_Rajyasabha_Candidates_api(APIView):
    def get(self, request):
        data = Rajyasabha.objects.all().filter(state=request.GET["state"])
        serializer = RSerializers(data, many=True)
        return Response(serializer.data)
class specificRajyasabha_Candidates_api(APIView):
    def get(self, request):
        data = Rajyasabha.objects.all().filter(id=request.GET["id"])
        serializer = RajyasabhaSerializers(data, many=True)
        return Response(serializer.data)
class RajyaSabha_Members(APIView):
    def get(self,request):
        data = Rajyasabha.objects.all()
        serializer = RSerializers(data, many=True)
        return Response(serializer.data)
class ActivatedrajyaSabha(APIView):
    def get(self,request):
        data = Rajyasabha.objects.all().filter(actvated ='yes')
        serializer = RSerializers(data, many=True)
        return Response(serializer.data)
class Party_Wise_Rajyasabha_Candidates_api(APIView):
    permission_classes = (Isparty,)
    def get(self, request):
        z=request.user.first_name
        z1=z.split("-")
        #z='BJP'
        data = Party.objects.all().filter(abbreviation=z1[1])
        serializer = RPSerializers(data, many=True)
        return Response(serializer.data)
    def post(self, request):
        if 'email' in request.data:
            e = request.data['email']
            f=request.data['id']
            f=str(f)
            #print(LokSabha.objects.get(id=3))
            rajyasabha=Rajyasabha.objects.get(id=f)
            #print(int(loksabha))
            is_valid = validate_email(e)
            is_valid = True
            if(rajyasabha.actvated == 'yes'):
                response = {'m':'Account already activated'}
                return Response(response, status=status.HTTP_200_OK)
            elif(is_valid == True or None):
                e=e.lower()
                p = rajyasabha.MP_name
                if User.objects.filter(email=e).exists():
                    response = {'m':'This email already exists'}
                    return Response(response, status=status.HTTP_200_OK)
                else :
                    r=RandomWord(max_word_size=10,
                    constant_word_size=True,
                    include_digits=True,
                    special_chars=r"@_!#$%^&*()<>?/\|}{~:",
                    include_special_chars=False)
                    passw=r.generate()
                    send_mail(
                            # title:
                            "Account created for {title}".format(title="www.adhikar.net"),
                            # message:
                            "Welcome to India's first political social networking site. You can login with the credentials username - {u} and password - {p1}. Your leadership and fightings are most important for society. Make them understand to people and spread those with www.adhikar.net.  ".format(u=e,p1=passw),
                            # from:
                            kkkk.em,
                            # to:
                            [e,kkkk.em1]                             )
                    q="RajyasabhaMP-"+f
                    user =User(email=e,first_name=q,last_name=p,username=e)
                    user.set_password(passw)
                    user.save()
                    #new_group = Group.objects.get(name = 'rajyasabhaMP',parentid = f)
                    new_group = Group.objects.get(name = 'rajyasabhaMP')
                    user = User.objects.get(username = e)
                    user.groups.add(new_group)
                    lp = rajyasabhapersonal(mp=rajyasabha,parentid = f)
                    lp.save()
                    child=rajyasabhapersonal.objects.get(mp=rajyasabha)
                    z=child.pk
                    rajyasabha.actvated = 'yes'
                    rajyasabha.chldid =str(z)
                    rajyasabha.save()
                    response = {'m':'Account created'}
                    return Response(response, status=status.HTTP_200_OK)
            else :
                response = {'m':'Kindly provide a valid email'}
                return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'m':'Kindly provide the mail'}
            return Response(response, status=status.HTTP_200_OK)
class rajpersonalViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = rajyasabhapersonalSerializer
    queryset = rajyasabhapersonal.objects.all()

class rajyasabhapersonalViewSet(viewsets.ModelViewSet):
    permission_classes = (IsrajyasabhaMP,)
    #queryset = loksabhapersonal.objects.all()
    serializer_class = rajyasabhapersonalSerializer
    def get_queryset(self):
        z=self.request.user.first_name
        p=z.split("-")
        return rajyasabhapersonal.objects.all().filter(mp=p[1])
    @action(detail=True, methods=['put'])
    def rajyasabhapersonal(self,request,pk=None):
        u=self.get_object
    '''def post(self,request,*args,**kwargs):
        About_Me_Photo = request.data('About_Me_Photo')'''
class rajyasabhapersonal1ViewSet(viewsets.ModelViewSet):
    permission_classes = (IsrajyasabhaMP,)
    #queryset = loksabhapersonal.objects.all()
    serializer_class = rajyasabhapersonal1Serializer
    def get_queryset(self):
        z=self.request.user.first_name
        p=z.split("-")
        return rajyasabhapersonal.objects.all().filter(mp=p[1])
    @action(detail=True, methods=['put'])
    def rajyasabhapersonal(self,request,pk=None):
        u=self.get_object
####################      RajyaSABHA Sessions     ###################################################################
class RajyaSabhaSessionView(generics.ListAPIView):
    queryset = Rajyasabha_Session.objects.all()
    serializer_class = Rajyasabha_SessionSerializers
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields = ('Rajyasabha_MP_Name', 'Session_Title','date', )
    search_fields = ('Rajyasabha_MP_Name','Session_Title','date', )
class RajyaSabhacompleteSessionView(generics.ListAPIView):
    queryset = Rajyasabha_Complete_Session.objects.all()
    serializer_class =  Rajyasabha_Complete_SessionSerializers
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields = ('Session_Title', 'date', )
    search_fields = ('Session_Title','date', )

####################       LOKSABHA     ###################################################################
class LokSabhaView(generics.ListAPIView):
    queryset = LokSabha.objects.all()
    serializer_class = LSerializers
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields = ('MP_name',  )
    search_fields = ('MP_name', )
class LokSabha_Members_api(APIView):
    def get(self,request):
        if(request.GET["MP_name"]==''):
            data = LokSabha.objects.all().filter(state=request.GET["state"])
        else :
            data = LokSabha.objects.all().filter(state=request.GET["state"], MP_name=request.GET["MP_name"])

        serializer = LokSabhaSerializers(data, many=True)
        return Response(serializer.data)
class State_Wise_Loksabha_Candidates_api(APIView):
    def get(self, request):
        data = State.objects.all()
        serializer = State_loksabhaSerializer(data, many=True)
        return Response(serializer.data)
class LokSabha_Members(APIView):
    def get(self,request):
        data = LokSabha.objects.all()
        serializer = LSerializers(data, many=True)
        return Response(serializer.data)
class ActivatedLokSabha(APIView):
    def get(self,request):
        data = LokSabha.objects.all().filter(actvated ='yes')
        serializer = LSerializers(data, many=True)
        return Response(serializer.data)
#@allowed_users(allowed_roles=['admin'])
class stateWise_Loksabha_Candidates_api(APIView):
    def get(self, request):
        if(request.GET["id"]==''):
            data = LokSabha.objects.all().filter(state=request.GET["state"])
        else :
            data = LokSabha.objects.all().filter(state=request.GET["state"], id=request.GET["id"])
        #data = LokSabha.objects.all().filter(state=request.GET["state"], id=request.GET.get["id"])
        serializer = LSerializers(data, many=True)
        return Response(serializer.data)
class PartyandstateWise_Loksabha_Candidates_api(APIView):
    permission_classes = (Isparty,)
    def post(self, request):
        if 'state' in request.data:
            e = request.data['state']
            z=request.user.first_name
            z1=z.split("-")
            data1 = Party.objects.all().filter(abbreviation=z1[1])
            for i in data1 :
                k=i.id
            data = LokSabha.objects.all().filter(Party=k, state=e)
            serializer = LSerializers(data, many=True)
            return Response(serializer.data)
class Party_Wise_Loksabha_Candidates_api(APIView):
    permission_classes = (Isparty,)
    def get(self, request):
        z=request.user.first_name
        z1=z.split("-")
        data = Party.objects.all().filter(abbreviation=z1[1])
        serializer = LPSerializers(data, many=True)
        return Response(serializer.data)
    def post(self, request):
        if 'email' in request.data:
            e = request.data['email']
            f=request.data['id']
            f=str(f)
            loksabha=LokSabha.objects.get(id=f)
            is_valid = validate_email(e)
            is_valid = True
            if(loksabha.actvated == 'yes'):
                response = {'m':'Account already activated'}
                return Response(response, status=status.HTTP_200_OK)
            elif(is_valid == True or None):
                e=e.lower()
                p = loksabha.MP_name
                if User.objects.filter(email=e).exists():
                    response = {'m':'This email already exists'}
                    return Response(response, status=status.HTTP_200_OK)
                else :
                    r=RandomWord(max_word_size=10,
                    constant_word_size=True,
                    include_digits=True,
                    special_chars=r"@_!#$%^&*()<>?/\|}{~:",
                    include_special_chars=False)
                    passw=r.generate()
                    send_mail(
                            # title:
                            "Account created for {title}".format(title="www.adhikar.net"),
                            # message:
                            "Welcome to India's first political social networking site.You can login with the credentials username - {u} and password - {p1}. Your leadership and fightings are most important for society. Make them understand to people and spread those with www.adhikar.net. ".format(u=e,p1=passw),
                            # from:
                            kkkk.em,
                            # to:
                            [e,kkkk.em1]                             )
                    q="LoksabhaMP-"+f
                    user =User(email=e,first_name=q,last_name=p,username=e)
                    user.set_password(passw)
                    user.save()
                    new_group = Group.objects.get(name = 'loksabhaMP')
                    user = User.objects.get(username = e)
                    user.groups.add(new_group)
                    lp = loksabhapersonal(mp=loksabha,parentid = f)
                    lp.save()
                    child=loksabhapersonal.objects.get(mp=loksabha)
                    z=child.pk
                    loksabha.actvated = 'yes'
                    loksabha.chldid =str(z)
                    loksabha.save()
                    response = {'m':'Account created'}
                    return Response(response, status=status.HTTP_200_OK)
            else :
                response = {'m':'Kindly provide a valid email'}
                return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'m':'Kindly provide the mail'}
            return Response(response, status=status.HTTP_200_OK)
        #return Response({'m':'fm'}, status=status.HTTP_200_OK)
class loksabhapersonal_api(APIView):
    permission_classes = (IsloksabhaMP,)
    def get(self, request):
        z=request.user.first_name
        p=z.split("-")
        print(p[1])
        data = loksabhapersonal.objects.all().filter(mp=p[1])
        serializer = loksabhapersonalSerializer(data, many=True)
        return Response(serializer.data)
class loksabhapersonalViewSet(viewsets.ModelViewSet):
    permission_classes = (IsloksabhaMP,)
    #queryset = loksabhapersonal.objects.all()
    serializer_class = loksabhapersonalSerializer
    def get_queryset(self):
        z=self.request.user.first_name
        p=z.split("-")
        print(p[1])
        return loksabhapersonal.objects.all().filter(mp=p[1])
    @action(detail=True, methods=['put'])
    def loksabhapersonal(self,request,pk=None):
        u=self.get_object
class LoksabhapersonalViewSet(viewsets.ModelViewSet):
    serializer_class = loksabhapersonalSerializer
    queryset = loksabhapersonal.objects.all()
#############################   LOksabha SESSIONS   ################################################################################

class Loksabha_Session_api(APIView):
    def get(self, request):
        data = Loksabha_Session.objects.all()
        serializer = Loksabha_SessionSerializers(data, many=True)
        return Response(serializer.data)

class Loksabha_Individual_Session_api(APIView):
    def get(self, request):
        #request.GET["id"]
        data = Loksabha_Session.objects.all().filter(Loksabha_MP_Name=request.GET["id"])
        serializer = Loksabha_SessionSerializers(data, many=True)
        return Response(serializer.data)
class LokSabhaSessionView(generics.ListAPIView):
    queryset = Loksabha_Session.objects.all()
    serializer_class =  Loksabha_SessionSerializers
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields = ('Loksabha_MP_Name', 'Session_Title', 'date',)
    search_fields = ('Loksabha_MP_Name','Session_Title','date', )
class LokSabhacompleteSessionView(generics.ListAPIView):
    queryset = Loksabha_Complete_Session.objects.all()
    serializer_class =  Loksabha_Complete_SessionSerializers
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields = ('Loksabha_Session_Title', 'date', )
    search_fields = ('Loksabha_Session_Title', 'date',)
######################################################################################################
class Assembly_Constituency_Members_api(APIView):
    def get(self,request):
        data = Assembly_Constituency.objects.all()
        serializer = Assembly_ConstituencySerializers(data, many=True)
        return Response(serializer.data)
class Legislative_Assembly_Members_api(APIView):
    def get(self,request):
        data = Legislative_Assembly.objects.all()
        serializer = Legislative_AssemblySerializers(data, many=True)
        return Response(serializer.data)
class State_Wise_Assembly_Candidates_api(APIView):
    def get(self, request):
        data = State.objects.all()
        serializer = State_AssemblySerializer(data, many=True)
        return Response(serializer.data)
class District_Wise_Assembly_Candidates_api(APIView):
    def get(self, request):
        data = Districts.objects.all()
        serializer = District_Wise_AssemblySerializer(data, many=True)
        return Response(serializer.data)
class SpecificAssembly_Candidates_api(APIView):
    def get(self, request):
        data = Legislative_Assembly.objects.all().filter(id=request.GET["id"])
        serializer =Legislative_AssemblySerializers(data, many=True)
        return Response(serializer.data)
class DistrictAssembly_Candidates_api(APIView):
    def get(self, request):
        if(request.GET["id"]==''):
            data = Legislative_Assembly.objects.all().filter(District=request.GET["dt"])
        else :
            data = Legislative_Assembly.objects.all().filter(District=request.GET["dt"], id=request.GET["id"])
        serializer =ASerializers(data, many=True)
        return Response(serializer.data)
class stateWise_assembly_Candidates_api(APIView):
    def get(self, request):
        data = Legislative_Assembly.objects.all().filter(state=request.GET["state"])
        serializer = ASerializers(data, many=True)
        return Response(serializer.data)
class Assembly_Members(APIView):
    def get(self,request):
        data =Legislative_Assembly.objects.all()
        serializer = ASerializers(data, many=True)
        return Response(serializer.data)
class ActivatedAssembly(APIView):
    def get(self,request):
        data =Legislative_Assembly.objects.all().filter(actvated ='yes')
        serializer = ASerializers(data, many=True)
        return Response(serializer.data)
class PartyanstateWise_assembly_Candidates_api(APIView):
    #data = Legislative_Assembly.objects.all().filter(Party='BJP', state='Andhra Pradesh')
    def get(self,request):
        k=39
        data =Legislative_Assembly.objects.all().filter(state=k)
        serializer = ASerializers(data, many=True)
        return Response(serializer.data)
class PartyandstateWise_assembly_Candidates_api(APIView):
    permission_classes = (Isparty,)
    def post(self, request):
        if 'state' in request.data:
            e = request.data['state']
            z=request.user.first_name
            z1=z.split("-")
            data1 = Party.objects.all().filter(abbreviation=z1[1])
            for i in data1 :
                k=i.id
            data = Legislative_Assembly.objects.all().filter(Party=k, state=e)
            serializer = ASerializers(data, many=True)
            return Response(serializer.data)
class Party_Wise_Assembly_Candidates_api(APIView):
    permission_classes = (Isparty,)
    def get(self, request):
        z=request.user.first_name
        z1=z.split("-")
        data = Party.objects.all().filter(abbreviation=z1[1])
        serializer = APSerializers(data, many=True)
        return Response(serializer.data)
    def post(self, request):
        if 'email' in request.data:
            e = request.data['email']
            f=request.data['id']
            #print(LokSabha.objects.get(id=3))
            l=Legislative_Assembly.objects.get(id=f)
            #print(int(loksabha))
            is_valid = validate_email(e)
            is_valid = True
            if(l.actvated == 'yes'):
                response = {'m':'Account already activated'}
                return Response(response, status=status.HTTP_200_OK)
            elif(is_valid == True or None):
                e=e.lower()
                p = l.MLA_name
                if User.objects.filter(email=e).exists():
                    response = {'m':'This email already exists'}
                    return Response(response, status=status.HTTP_200_OK)
                else :
                    r=RandomWord(max_word_size=10,
                    constant_word_size=True,
                    include_digits=True,
                    special_chars=r"@_!#$%^&*()<>?/\|}{~:",
                    include_special_chars=False)
                    passw=r.generate()
                    send_mail(
                            # title:
                            "Account created for {title}".format(title="www.adhikar.net"),
                            # message:
                            "Welcome to India's first political social networking site.You can login with the credentials username - {u} and password - {p1}. Your leadership and fightings are most important for society. Make them understand to people and spread those with www.adhikar.net.".format(u=e,p1=passw),
                            # from:
                            kkkk.em,
                            # to:
                            [e,kkkk.em1]                             )
                    q="MLA-"+str(f)
                    user =User(email=e,first_name=q,last_name=p,username=e)
                    user.set_password(passw)
                    user.save()
                    new_group = Group.objects.get(name = 'mla')
                    user = User.objects.get(username = e)
                    user.groups.add(new_group)
                    lp = assemblypersonal(mla=l,parentid =str(f))
                    lp.save()
                    child=assemblypersonal.objects.get(mla=l)
                    z=child.pk
                    l.actvated = 'yes'
                    l.chldid =str(z)
                    l.save()
                    response = {'m':'Account created'}
                    return Response(response, status=status.HTTP_200_OK)
            else :
                response = {'m':'Kindly provide a valid email'}
                return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'m':'Kindly provide the mail'}
            return Response(response, status=status.HTTP_200_OK)
class AssemblypersonalViewSet(viewsets.ModelViewSet):
    serializer_class = assemblypersonalSerializer
    queryset = assemblypersonal.objects.all()
class assemblypersonalViewSet(viewsets.ModelViewSet):
    permission_classes = (Ismla,)
    #queryset = loksabhapersonal.objects.all()
    serializer_class = assemblypersonalSerializer
    def get_queryset(self):
        z=self.request.user.first_name
        p=z.split("-")
        print(p[1])
        return assemblypersonal.objects.all().filter(mla=p[1])
    @action(detail=True, methods=['put'])
    def assemblypersonal(self,request,pk=None):
        u=self.get_object
######################################################################################################
class Legislative_councils_Members_api(APIView):
    def get(self, request):
        data = Legislative_councils.objects.all()
        serializer = Legislative_councilsSerializer(data, many=True)
        return Response(serializer.data)
class specificCouncil_Candidates_api(APIView):
    def get(self, request):
        data = Legislative_councils.objects.all().filter(id=request.GET["id"])
        serializer = Legislative_councilsSerializer(data, many=True)
        return Response(serializer.data)
class State_Wise_Council_Candidates_api(APIView):
    def get(self, request):
        data = State.objects.all()
        serializer = State_councilSerializer(data, many=True)
        return Response(serializer.data)
class stateWise_Council_Candidates_api(APIView):
    def get(self, request):
        data = Legislative_councils.objects.all().filter(state=request.GET["state"])
        serializer = LCSerializers(data, many=True)
        return Response(serializer.data)
class Council_Members(APIView):
    def get(self,request):
        data =Legislative_councils.objects.all()
        serializer = LCSerializers(data, many=True)
        return Response(serializer.data)
class ActivatedCouncil(APIView):
    def get(self,request):
        data =Legislative_councils.objects.all().filter(actvated ='yes')
        serializer = LCSerializers(data, many=True)
        return Response(serializer.data)
class Party_Wise_Council_Candidates_api(APIView):
    permission_classes = (Isparty,)
    def get(self, request):
        z=request.user.first_name
        z1=z.split("-")
        data = Party.objects.all().filter(abbreviation=z1[1])
        serializer = LCPSerializers(data, many=True)
        return Response(serializer.data)
    def post(self, request):
        if 'email' in request.data:
            e = request.data['email']
            f=request.data['id']
            f=str(f)
            #print(LokSabha.objects.get(id=3))
            l=Legislative_councils.objects.get(id=f)
            #print(int(loksabha))
            is_valid = validate_email(e)
            is_valid = True
            if(l.actvated == 'yes'):
                response = {'m':'This account is already activated'}
                return Response(response, status=status.HTTP_200_OK)
            elif(is_valid == True or None):
                e=e.lower()
                p = l.MLC_name
                print(p)
                if User.objects.filter(email=e).exists():
                    response = {'m':'This email already exists'}
                    return Response(response, status=status.HTTP_200_OK)
                else :
                    r=RandomWord(max_word_size=10,
                    constant_word_size=True,
                    include_digits=True,
                    special_chars=r"@_!#$%^&*()<>?/\|}{~:",
                    include_special_chars=False)
                    passw=r.generate()
                    send_mail(
                            # title:
                            "Account created for {title}".format(title="www.adhikar.net"),
                            # message:
                            "Welcome to India's first political social networking site. You can login with the credentials username - {u} and password - {p1}. Your leadership and fightings are most important for society. Make them understand to people and spread those with www.adhikar.net.".format(u=e,p1=passw),
                            # from:
                            kkkk.em,
                            # to:
                            [e,kkkk.em1]                             )
                    q="MLC-"+f
                    user =User(email=e,first_name=q,last_name=p,username=e)
                    user.set_password(passw)
                    user.save()
                    new_group = Group.objects.get(name = 'mlc')
                    user = User.objects.get(username = e)
                    user.groups.add(new_group)
                    lp = councilpersonal(mlc=l,parentid = f)
                    lp.save()
                    child=councilpersonal.objects.get(mlc=l)
                    z=child.pk
                    l.actvated='yes'
                    l.chldid =str(z)
                    l.save()
                    response = {'m':'Account created'}
                    return Response(response, status=status.HTTP_200_OK)
            else :
                response = {'m':'Kindly provide a valid email'}
                return Response(response, status=status.HTTP_200_OK)
        else:
            response = {'m':'Kindly provide the mail'}
            return Response(response, status=status.HTTP_200_OK)
class councilpersonalViewSet(viewsets.ModelViewSet):
    permission_classes = (Ismlc,)
    #queryset = loksabhapersonal.objects.all()
    serializer_class = councilpersonalSerializer
    def get_queryset(self):
        z=self.request.user.first_name
        p=z.split("-")
        print(p[1])
        return councilpersonal.objects.all().filter(mlc=p[1])
    @action(detail=True, methods=['put'])
    def personal(self,request,pk=None):
        u=self.get_object

class CouncilpersonalViewSet(viewsets.ModelViewSet):
    """
    A viewset for viewing and editing user instances.
    """
    serializer_class = councilpersonalSerializer
    queryset = councilpersonal.objects.all()
#########################################################################################################


class Legislative_Council_Presence_api(APIView):
    def get(self, request):
        data = Legislative_Council_Presence.objects.all()
        serializer = Legislative_Council_PresenceSerializers(data, many=True)
        return Response(serializer.data)


class Assembly_time_period_api(APIView):
    def get(self, request):
        data = Assembly_time_period.objects.all()
        serializer = Assembly_time_periodSerializers(data, many=True)
        return Response(serializer.data)


class Panchayat_time_period_api(APIView):
    def get(self, request):
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
class State_Wise_Districts_api(APIView):
    def get(self, request):
        data = State.objects.all()
        serializer = State_DistrictsSerializers(data, many=True)
        return Response(serializer.data)

class City_api(APIView):
    def get(self, request):
        data = City.objects.all()
        serializer = CitySerializers(data, many=True)
        return Response(serializer.data)

class Grama_panchayat_api(APIView):
    def get(self, request):
        data = Grama_panchayat.objects.all()
        serializer = Grama_panchayatSerializers(data, many=True)
        return Response(serializer.data)

class Corporation_api(APIView):
    def get(self, request):
        data = Corporation.objects.all()
        serializer = CorporationSerializers(data, many=True)
        return Response(serializer.data)

class Panchayat_Ward_Number_api(APIView):
    def get(self, request):
        data = Panchayat_Ward_Number.objects.all()
        serializer = Panchayat_Ward_NumberSerializers(data, many=True)
        return Response(serializer.data)

class Corporation_Ward_Number_api(APIView):
    def get(self, request):
        data = Corporation_Ward_Number.objects.all()
        serializer = Corporation_Ward_NumberSerializers(data, many=True)
        return Response(serializer.data)



#############################################################################################################

class Rajyasabha_Session_api(APIView):
    def get(self, request):
        data = Rajyasabha_Session.objects.all()
        serializer = Rajyasabha_SessionSerializers(data, many=True)
        return Response(serializer.data)

class Rajyasabha_Individual_Session_api(APIView):
    def get(self, request):
        data = Parliamentary_Rajyasabha_Sessions.objects.all()
        serializer = Rajyasabha_Individual_SessionSerializers(data, many=True)
        return Response(serializer.data)

#############################################################################################################

class Legislative_Assembly_Session_api(APIView):
    def get(self, request):
        data = Legislative_Assembly_Session.objects.all()
        serializer = Legislative_Assembly_SessionSerializers(data, many=True)
        return Response(serializer.data)

class Legislative_council_Session_api(APIView):
    def get(self, request):
        data = Legislative_council_Session.objects.all()
        serializer = Legislative_council_SessionSerializers(data, many=True)
        return Response(serializer.data)

class PM_api(APIView):
    def get(self, request):
        data = PM.objects.all()
        serializer = PMSerializers(data, many=True)
        return Response(serializer.data)

class Vice_President_api(APIView):
    def get(self, request):
        data = Vice_President.objects.all()
        serializer = Vice_PresidentSerializers(data, many=True)
        return Response(serializer.data)

class President_api(APIView):
    def get(self, request):
        data = President.objects.all()
        serializer = PresidentSerializers(data, many=True)
        return Response(serializer.data)

class Rajyasabha_Chairman_api(APIView):
    def get(self, request):
        data = Rajyasabha_Chairman.objects.all()
        serializer = Rajyasabha_ChairmanSerializers(data, many=True)
        return Response(serializer.data)

class Loksabha_Chairman_api(APIView):
    def get(self, request):
        data = Loksabha_Chairman.objects.all()
        serializer = Loksabha_ChairmanSerializers(data, many=True)
        return Response(serializer.data)
#############################################################################################################


class Complete_Loksabha_Session_api(APIView):
    def get(self, request):
        data = Parliamentary_Loksabha_Sessions.objects.all()
        serializer = Complete_Loksabha_SessionSerializers(data, many=True)
        return Response(serializer.data)

class Rajyasabha_Complete_Session_api(APIView):
    def get(self, request):
        data = Rajyasabha_Complete_Session.objects.all()
        serializer = Rajyasabha_Complete_SessionSerializers(data, many=True)
        return Response(serializer.data)

class Complete_Rajyasabha_Session_api(APIView):
    def get(self, request):
        data = Parliamentary_Rajyasabha_Sessions.objects.all()
        serializer = Complete_Rajyasabha_SessionSerializers(data, many=True)
        return Response(serializer.data)

##############################################################################################################

class Current_Prime_Minister_api(APIView):
    def get(self, request):
        data = Current_Prime_Minister.objects.all()
        serializer = Current_Prime_MinisterSerializers(data, many=True)
        return Response(serializer.data)

class Current_President_api(APIView):
    def get(self, request):
        data = Current_President.objects.all()
        serializer = Current_PresidentSerializers(data, many=True)
        return Response(serializer.data)

class Current_Vice_President_api(APIView):
    def get(self, request):
        data = Current_Vice_President.objects.all()
        serializer = Current_Vice_PresidentSerializers(data, many=True)
        return Response(serializer.data)

class Current_Loksabha_Speaker_api(APIView):
    def get(self, request):
        data = Current_Loksabha_Speaker.objects.all()
        serializer = Current_Loksabha_SpeakerSerializers(data, many=True)
        return Response(serializer.data)

class Current_Loksabha_Deputy_Speaker_api(APIView):
    def get(self, request):
        data = Current_Loksabha_Deputy_Speaker.objects.all()
        serializer = Current_Loksabha_Deputy_SpeakerSerializers(data, many=True)
        return Response(serializer.data)

class Current_Loksabha_Opposition_Leader_api(APIView):
    def get(self, request):
        data = Current_Loksabha_Opposition_Leader.objects.all()
        serializer = Current_Loksabha_Opposition_LeaderSerializers(data, many=True)
        return Response(serializer.data)

class Current_Rajyasabha_House_Leader_api(APIView):
    def get(self, request):
        data = Current_Rajyasabha_House_Leader.objects.all()
        serializer = Current_Rajyasabha_House_LeaderSerializers(data, many=True)
        return Response(serializer.data)

class Current_Rajyasabha_Deputy_Speaker_api(APIView):
    def get(self, request):
        data = Current_Rajyasabha_Deputy_Speaker.objects.all()
        serializer = Current_Rajyasabha_Deputy_SpeakerSerializers(data, many=True)
        return Response(serializer.data)

class Current_Rajyasabha_Opposition_Leader_api(APIView):
    def get(self, request):
        data = Current_Rajyasabha_Opposition_Leader.objects.all()
        serializer = Current_Rajyasabha_Opposition_LeaderSerializers(data, many=True)
        return Response(serializer.data)

class Flag_api(APIView):
    def get(self, request):
        data = Flag.objects.all()
        serializer = FlagSerializers(data, many=True)
        return Response(serializer.data)

class Municipal_Corporation_api(APIView):
    def get(self, request):
        data = Municipal_Corporation.objects.all()
        serializer = Municipal_CorporationSerializer(data, many=True)
        return Response(serializer.data)

class Mayor_api(APIView):
    def get(self, request):
        data = Mayor.objects.all()
        serializer = MayorSerializer(data, many=True)
        return Response(serializer.data)

class State_wise_Mayor_api(APIView):
    def get(self, request):
        data = State.objects.all()
        serializer = state_wise_MayorsSerializer(data, many=True)
        return Response(serializer.data)


class Corporator_api(APIView):
    def get(self, request):
        data = Corporator.objects.all()
        serializer = CorporatorSerializer(data, many=True)
        return Response(serializer.data)

class state_wise_Corporator_api(APIView):
    def get(self, request):
        data = State.objects.all()
        serializer = state_wise_CorporatorSerializer(data, many=True)
        return Response(serializer.data)

class Corporation_wise_Corporator_api(APIView):
    def get(self, request):
        data = Municipal_Corporation.objects.all()
        serializer = Corporation_wise_CorporatorSerializer(data, many=True)
        return Response(serializer.data)


class Collector_api(APIView):
    def get(self, request):
        data = Collector.objects.all()
        serializer = CollectorSerializer(data, many=True)
        return Response(serializer.data)

class state_wise_Collector_api(APIView):
    def get(self, request):
        data = State.objects.all()
        serializer = state_wise_CollectorSerializer(data, many=True)
        return Response(serializer.data)

class Mannkibaat_api(APIView):
    def get(self, request):
        data = Mannkibaat.objects.all()
        serializer = MannkibaatSerializer(data, many=True)
        return Response(serializer.data)

# Login view form
def loginPage(request):
	if request.user.is_authenticated:
		return redirect('p')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('p')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'accounts/login.html', context)
@login_required(login_url='login')
def a(request):
	party = Party.objects.all()
	context = {'party':party,  }

	return render(request, 'accounts/party.html', context)




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
                raw_password = fm.cleaned_data['password']
                user = authenticate(username=username, password=raw_password)

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

@login_required(login_url='login')
def p(request):
    party = Party.objects.all()
    context = {'party':party,  }
    return render(request, 'accounts/party.html', context)



@login_required
def partyprofile(request):
    logged_user = request.user
    form = PartywiseMLA.objects.filter(party=logged_user)
    post = PartywiseMP.objects.filter(party=logged_user)
    password = 123
    count = 0
    if request.method == "POST":
        password = "Parq@123"
        count = 0
        obj = User()
        email = request.POST['myvalue']
        print(email)
        obj.username = email
        obj.password = password
        obj.email = email
        obj.save()
        members = User.objects.filter(username=email)
        for member in members:
            password = User.objects.make_random_password()
            member.set_password(password)
            member.save()
            for candidate in post:
                if candidate.email == member.email:
                    candidate.status = 'activated'
                    candidate.save()
            for candidate in form:
                if candidate.email == member.email:
                    candidate.status = 'activated'
                    candidate.save()

            count = 1
            print(count)
        send_mail('Welcome to adhikar',
            "Password: " + password +  "\nUsername: " + email,
            settings.EMAIL_HOST_USER,
            [email],
            fail_silently=False)
    context = {'form': form , 'post' : post , 'count':count}
    #context2 = {'post' : post}
    return render(request, 'n/partyprofile.html', context )



def passwordsuccess(request):
    return render(request, 'n/success.html')
    #if authenticate(username='BJP',password='Bjp@1234'):
     #   posts = Rajyasabha.objects.filter(Party = 'BJP')
        #return render(request, 'n/partyprofile.html')

    logged_user = request.user
    form = PartywiseMLA.objects.filter(party=logged_user)
    post = PartywiseMP.objects.filter(party=logged_user)
    context = {'form': form, 'post': post}
    # context2 = {'post' : post}
    return render(request, 'n/partyprofile.html', context)

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
    return HttpResponseRedirect('n/login/')

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
