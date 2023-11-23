from django.urls import path
from . import views

urlpatterns = [
    path('call-function/', views.call_function, name='call_function'),
]
