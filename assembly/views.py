from django.shortcuts import render
from .models import *
from .models import Legislative_Assembly1 as la
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import SearchFilter
import pandas as pd
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
import uuid
from datetime import datetime
from django.http import JsonResponse
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
def export11(request):
    Legislative_Assembly1_objs = la.objects.filter(state=39)
    #serializer = Legislative_AssemblySerializer(Legislative_Assembly1_objs,many=True)
    pd.DataFrame(Legislative_Assembly1_objs).to_excel("output.xlsx")
    return JsonResponse({'status':200})
class ExportImportExcelView(APIView):
    def get(self,request):
        m = request.GET.get('k')
        Legislative_Assembly1_objs = la.objects.filter(state=m)
        serializer = Legislative_AssemblySerializer(Legislative_Assembly1_objs,many=True)
        df = pd.DataFrame(serializer.data)
        z = df.to_dict()
        print(z)
        #excelupload.objects.create(excelfileupload = "/media/mohan/mn/mnew/m/123.xlsx")
        return Response({'k':z})
