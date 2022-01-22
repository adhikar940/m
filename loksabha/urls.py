from django.urls import include, path
from . views import *
urlpatterns = [
path('loksbhadata1/', LokSabhaView1.as_view()),
path('LoksabhaindividualSessionapi1/', LokSabhaSessionView1.as_view()),
path('LoksabhaCompleteSessionapi1/', LokSabhacompleteSessionView1.as_view()),
]
