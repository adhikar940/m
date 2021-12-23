from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from n import views as user_views
from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework.routers import DefaultRouter
from rest_framework import routers
from . import views
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token
from .views import PartyViewSet
#from auth.views import UpdateProfileView
router = DefaultRouter()



urlpatterns = [
    path('excel/', views.kapi.as_view()),
    path('', include(router.urls)),
    path('test1/',views.tmail),
    path('login/', views.loginPage, name="login"),
    path('Assemblyconstituencydata/', views.AssemblyconstituencyView.as_view()),
    #url(r'^personalimages/', user_views.personalimages_api.as_view()),
    ######################################## States ##################################################################
    url(r'^State_api/', user_views.State_api.as_view()),
    url(r'^Districts_api/', user_views.Districts_api.as_view()),
    url(r'^State_Wise_Districts_api/', user_views.State_Wise_Districts_api.as_view()),
    url(r'^City_api/', user_views.City_api.as_view()),
    url(r'^state_api/', user_views.State_api.as_view()),
    url(r'^states_api/', user_views.States_api.as_view()),

    ############################## Party ############################################################################
    path('partydata/', views.PartyView.as_view()),
    path('stateactivateparty/', views.stateactivateparty.as_view()),
    path('statepartyactivate/', views.statepartyapi.as_view()),
    #path('activatedstateparty/', views.statePartyViewSet.as_view()),
    url(r'^party_api/', user_views.Party_api.as_view()),
    url(r'^activatedparty/', user_views.Activatedparty.as_view()),
    url(r'^coalitionparty_api/', user_views.Coalition_Party_api.as_view()),


    ############################        Rajya Sabha           ####################################################
    url(r'^activatedrajyasabha/', user_views.ActivatedrajyaSabha.as_view()),
    url(r'^Rajyasabha_Candidates_api/', user_views.Rajyasabha_Members_api.as_view()),
    url(r'^Rajyasabhapresedent/', user_views.Rajyasabhapresedent.as_view()),
    url(r'^State_Wise_Rajyasabha_Candidates_api/', user_views.State_Wise_Rajyasabha_Candidates_api.as_view()),
    url(r'^stateWise_Rajyasabha_Candidates_api/', user_views.stateWise_Rajyasabha_Candidates_api.as_view()),
    url(r'^specificRajyasabha_Candidates_api/', user_views.specificRajyasabha_Candidates_api.as_view()),
    url(r'^party_raj_api/', user_views.Party_Wise_Rajyasabha_Candidates_api.as_view()),
    path('RajyasabhaindividualSessionapi/', views.RajyaSabhaSessionView.as_view()),
    path('RajyasabhacompleteSessionapi/', views.RajyaSabhacompleteSessionView.as_view()),


    #####################################       Lok sabha   ######################################################################
    url(r'^activatedloksabha/', user_views.ActivatedLokSabha.as_view()),
    url(r'^LokSabha_Candidates_api/', user_views.LokSabha_Members_api.as_view()),
    url(r'^State_Wise_Loksabha_Candidates_api/', user_views.State_Wise_Loksabha_Candidates_api.as_view()),
    url(r'^stateWise_Loksabha_Candidates_api/', user_views.stateWise_Loksabha_Candidates_api.as_view()),
    url(r'^party_lok_api/', user_views.Party_Wise_Loksabha_Candidates_api.as_view()),
    url(r'^stateparty_lok_api/', user_views.PartyandstateWise_Loksabha_Candidates_api.as_view()),
    url(r'^lokpersonal_api/', user_views.loksabhapersonal_api.as_view()),
    path('loksbhadata/', views.LokSabhaView.as_view()),
    path('LoksabhaindividualSessionapi/', views.LokSabhaSessionView.as_view()),
    url(r'^LoksabhaCompleteSessionapi/', views.LokSabhacompleteSessionView.as_view()),
    #url(r'^lokpersonal/(?P<pk>[0-9]+)$', views.loksabhapersonal_detail),
    ###########################################################################################################
    url(r'^activatedassembly/', user_views.ActivatedAssembly.as_view()),
    url(r'^Assembly_Candidates_api/', user_views.Legislative_Assembly_Members_api.as_view()),
    url(r'^State_Wise_Assembly_Candidates_api/', user_views.State_Wise_Assembly_Candidates_api.as_view()),
    url(r'^District_Wise_Assembly_Candidates_api/', user_views.District_Wise_Assembly_Candidates_api.as_view()),
    url(r'^stateWise_Assembly_Candidates_api/', user_views.stateWise_assembly_Candidates_api.as_view()),
    url(r'^districtAssembly_Candidates_api/', user_views.DistrictAssembly_Candidates_api.as_view()),
    url(r'^party_assembly_api/', user_views.Party_Wise_Assembly_Candidates_api.as_view()),
    url(r'^partyandstateassembly_api/', user_views.PartyandstateWise_assembly_Candidates_api.as_view()),
    url(r'^specificAssembly_Candidates_api/', user_views.SpecificAssembly_Candidates_api.as_view()),

    ###########################################################################################################
url(r'^specificCouncils_Candidates_api/', user_views.specificCouncil_Candidates_api.as_view()),
    url(r'^Legislative_Councils_Candidates_api/', user_views.Legislative_councils_Members_api.as_view()),
    url(r'^State_Wise_Council_Candidates_api/', user_views.State_Wise_Council_Candidates_api.as_view()),
    url(r'^party_coucil_api/', user_views.Party_Wise_Council_Candidates_api.as_view()),
    url(r'^statewise_Council_Candidates_api/', user_views.stateWise_Council_Candidates_api.as_view()),
    url(r'^activatedcouncil/', user_views.ActivatedCouncil.as_view()),
    ##########################################################################################################

    url(r'^Assembly_time_period_api/', user_views.Assembly_time_period_api.as_view()),
    url(r'^Panchayat_time_period_api/', user_views.Panchayat_time_period_api.as_view()),
    url(r'^Municipal_time_period_api/', user_views.Municipal_time_period_api.as_view()),

    url(r'^Grama_panchayat_api/', user_views.Grama_panchayat_api.as_view()),
    url(r'^Corporation_api/', user_views.Corporation_api.as_view()),
    url(r'^Panchayat_Ward_Number_api/', user_views.Panchayat_Ward_Number_api.as_view()),
    url(r'^Corporation_Ward_Number_api/', user_views.Corporation_Ward_Number_api.as_view()),

    ############################################################################################################
    #               Loksabha & Rajyasabha Individual APIs

    url(r'^loksabhasession_api/', user_views.Loksabha_Session_api.as_view()),
    url(r'^Loksabha_Individual_Session_api/', user_views.Loksabha_Individual_Session_api.as_view()),

    url(r'^rajyasabhasession_api/', user_views.Rajyasabha_Session_api.as_view()),
    url(r'^Rajyasabha_Individual_Session_api/', user_views.Rajyasabha_Individual_Session_api.as_view()),

    url(r'^Legislative_Assembly_Session_api/', user_views.Legislative_Assembly_Session_api.as_view()),
    url(r'^Legislative_council_Session_api/', user_views.Legislative_council_Session_api.as_view()),

    #############################################################################################################
    #                         Session apis
    url(r'^PM_api/', user_views.PM_api.as_view()),
    url(r'^President_api/', user_views.President_api.as_view()),
    url(r'^Vice_President_api/', user_views.Vice_President_api.as_view()),
    url(r'^Rajyasabha_Chairman_api/', user_views.Rajyasabha_Chairman_api.as_view()),
    url(r'^Loksabha_Chairman_api/', user_views.Loksabha_Chairman_api.as_view()),

    #############################################################################################################
    #                        Loksabha & Rajyasabha Complete APIs


    url(r'^Complete_Loksabha_Session_api/', user_views.Complete_Loksabha_Session_api.as_view()),

    url(r'^Rajyasabha_Complete_Session_api/', user_views.Rajyasabha_Complete_Session_api.as_view()),
    url(r'^Complete_Rajyasabha_Session_api/', user_views.Complete_Rajyasabha_Session_api.as_view()),

    #############################################################################################################
    #               Parliamentary Current Leaders APIs

    url(r'^Current_Prime_Minister_api/', user_views.Current_Prime_Minister_api.as_view()),
    url(r'^Current_President_api/', user_views.Current_President_api.as_view()),
    url(r'^Current_Vice_President_api/', user_views.Current_Vice_President_api.as_view()),
    url(r'^Current_Loksabha_Speaker_api/', user_views.Current_Loksabha_Speaker_api.as_view()),
    url(r'^Current_Loksabha_Deputy_Speaker_api/', user_views.Current_Loksabha_Deputy_Speaker_api.as_view()),
    url(r'^Current_Loksabha_Opposition_Leader_api/', user_views.Current_Loksabha_Opposition_Leader_api.as_view()),
    url(r'^Current_Rajyasabha_House_Leader_api/', user_views.Current_Rajyasabha_House_Leader_api.as_view()),
    url(r'^Current_Rajyasabha_Deputy_Speaker_api/', user_views.Current_Rajyasabha_Deputy_Speaker_api.as_view()),
    url(r'^Current_Rajyasabha_Opposition_Leader_api/', user_views.Current_Rajyasabha_Opposition_Leader_api.as_view()),

    #############################################################################################################

    url(r'^Flag_api/', user_views.Flag_api.as_view()),

    #############################################################################################################

    url(r'^Municipal_Corporation_api/', user_views.Municipal_Corporation_api.as_view()),
    url(r'^Mayor_api/', user_views.Mayor_api.as_view()),
    url(r'^State_wise_Mayor_api/', user_views.State_wise_Mayor_api.as_view()),

    #############################################################################################################

    url(r'^Corporator_api/', user_views.Corporator_api.as_view()),
    url(r'^state_wise_Corporator_api/', user_views.state_wise_Corporator_api.as_view()),
    url(r'^Corporation_wise_Corporator_api/', user_views.Corporation_wise_Corporator_api.as_view()),

    #############################################################################################################
    url(r'^Collector_api/', user_views.Collector_api.as_view()),
    url(r'^Mannkibaat_api/', user_views.Mannkibaat_api.as_view()),
    url(r'^state_wise_Collector_api/', user_views.state_wise_Collector_api.as_view()),

]
