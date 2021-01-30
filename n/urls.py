from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from n import views as user_views
from django.conf.urls import url,include
from rest_framework.urlpatterns import format_suffix_patterns
from drf_multiple_model.views import ObjectMultipleModelAPIView
from rest_framework.routers import DefaultRouter
from .views import CarsAPIView

router = DefaultRouter()
router.register('car-specs', user_views.CarsAPIView, basename='car-specs')


urlpatterns = [
url(r'^', include(router.urls)),

url(r'^bihar_api/', user_views.Bihar_api.as_view()),
url(r'^dubbakka_api/', user_views.Dubbaka_api.as_view()),
url(r'^dubbakkawinner_api/', user_views.DubbakaWinner_api.as_view()),
url(r'^dubbakkarunner_api/', user_views.DubbakaRunner_api.as_view()),
url(r'^biharwinner_api/', user_views.BiharWinner_api.as_view()),
url(r'^biharrunner_api/', user_views.BiharRunner_api.as_view()),
url(r'^party_api/', user_views.Party_api.as_view()),
url(r'^coalitionparty_api/', user_views.Coalition_Party_api.as_view()),
url(r'^leading_api/', user_views.Leadingseats_api.as_view()),
url(r'^states_api/', user_views.States_api.as_view()),
url(r'^Rajyasabha_api/', user_views.Rajyasabha_api.as_view()),
#url(r'^cars/', user_views.CarsAPIView.as_view({'get': 'list'})),
url(r'^LokSabha_api/', user_views.LokSabha_api.as_view()),
url(r'^Assembly_api/', user_views.Assembly_api.as_view()),
url(r'^Legislative_Council_api/', user_views.Legislative_Council_api.as_view()),
url(r'^Assembly_time_period_api/', user_views.Assembly_time_period_api.as_view()),
url(r'^Panchayat_time_period_api/', user_views.Panchayat_time_period_api.as_view()),
url(r'^Municipal_time_period_api/', user_views.Municipal_time_period_api.as_view()),
url(r'^State_api/', user_views.State_api.as_view()),
url(r'^Districts_api/', user_views.Districts_api.as_view()),
url(r'^City_api/', user_views.City_api.as_view()),
url(r'^Grama_panchayat_api/', user_views.Grama_panchayat_api.as_view()),
url(r'^Corporation_api/', user_views.Corporation_api.as_view()),
url(r'^Panchayat_Ward_Number_api/', user_views.Panchayat_Ward_Number_api.as_view()),
url(r'^Corporation_Ward_Number_api/', user_views.Corporation_Ward_Number_api.as_view()), 
url(r'^loksabhasession_api/', user_views.Loksabha_Session_api.as_view()),
url(r'^rajyasabhasession_api/', user_views.Rajyasabha_Session_api.as_view()),
url(r'^legislative_assembly_api/', user_views.Legislative_Assembly_Session_api.as_view()),
url(r'^legislative_counsil_api/', user_views.Legislative_counsil_Session_api.as_view()),
url(r'^PM_api/', user_views.PM_api.as_view()),
url(r'^President_api/', user_views.President_api.as_view()),
url(r'^Vice_President_api/', user_views.Vice_President_api.as_view()),
url(r'^Rajyasabha_Chairman_api/', user_views.Rajyasabha_Chairman_api.as_view()),
url(r'^Locksabha_Chairman_api/', user_views.Locksabha_Chairman_api.as_view()),
url(r'^Locksabha_Complete_Session_api/', user_views.Locksabha_Complete_Session_api.as_view()),
url(r'^Rajyasabha_Complete_Session_api/', user_views.Rajyasabha_Complete_Session_api.as_view()),



]
