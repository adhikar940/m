from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path
from n import views as user_views
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns



urlpatterns = [

url(r'^bihar_api/',user_views.Bihar_api.as_view()),
url(r'^dubbakka_api/',user_views.Dubbaka_api.as_view()),
]