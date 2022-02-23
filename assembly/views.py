from django.shortcuts import render
from .models import *
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter
class Assembly_Constituency(generics.ListAPIView):
    queryset = Assembly_Constituency1.objects.all()
    serializer_class = Assembly_ConstituencySerializers1
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields = ('State', 'Districts', 'Assembly_Constituency_Name' )
    search_fields = ('State', 'Districts', 'Assembly_Constituency_Name' )
class Legislative_Assembly1(generics.ListAPIView):
    queryset = Legislative_Assembly1.objects.all()
    serializer_class =  Legislative_AssemblySerializers1
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields = ('state','District', 'constituency_name', 'MLA_name',)
    search_fields = ('state','District', 'constituency_name', 'MLA_name', )
class assemblypersonal1(generics.ListAPIView):
    queryset = assemblypersonal1.objects.all()
    serializer_class =  assemblypersonalSerializer1
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields = ('mla' )
    search_fields = ('mla')
class assemblyterm(generics.ListAPIView):
    queryset = assemblyterm.objects.all()
    serializer_class =  assemblytermSerializers
    filter_backends = (DjangoFilterBackend,SearchFilter)
    filter_fields = ('mla' )
    search_fields = ('mla')
