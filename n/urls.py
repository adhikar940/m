from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from n import views as user_views
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from drf_multiple_model.views import ObjectMultipleModelAPIView


urlpatterns = [

url(r'^bihar_api/',user_views.Bihar_api.as_view()),
url(r'^dubbakka_api/',user_views.Dubbaka_api.as_view()),
url(r'^dubbakkawinner_api/',user_views.DubbakaWinner_api.as_view()),
url(r'^dubbakkarunner_api/',user_views.DubbakaRunner_api.as_view()),
url(r'^biharwinner_api/',user_views.BiharWinner_api.as_view()),
url(r'^biharrunner_api/',user_views.BiharRunner_api.as_view()),
url(r'^party_api/',user_views.Party_api.as_view()),
url(r'^coalitionparty_api/',user_views.Coalition_Party_api.as_view()),
url(r'^leading_api/',user_views.Leadingseats_api.as_view()),
url(r'^states_api/', user_views.States_api.as_view()),
url(r'^Rajyasabha_api/', user_views.Rajyasabha_api.as_view()),
url(r'^LokSabha_api/', user_views.LokSabha_api.as_view()),
url(r'^Assembly_time_period_api/', user_views.Assembly_time_period_api.as_view()),
url(r'^Panchayat_time_period_api/', user_views.Panchayat_time_period_api.as_view()),
url(r'^Municipal_time_period_api/', user_views.Municipal_time_period_api.as_view()),
]