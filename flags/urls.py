from django.urls import include, path
from . views import *
urlpatterns = [
path('flag/', flagView.as_view()),
path('flag1/', flag1View.as_view()),
]
