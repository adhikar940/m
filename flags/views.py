from django.shortcuts import render
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter
from rest_framework import viewsets
class flagView(generics.ListAPIView):
    queryset = flag.objects.all()
    serializer_class = flagSerializers
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields = ('color','Highlight'  )
    search_fields = ('color','Highlight'  )
class flag1View(generics.ListAPIView):
    queryset = flag1.objects.all()
    serializer_class = flag1Serializers
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields = ('name','activate', )
    search_fields = ('name','activate', )
