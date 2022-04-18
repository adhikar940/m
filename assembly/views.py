from django.shortcuts import render
from django.http import HttpResponse
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
from n.models import *
from io import BytesIO
from django_pandas.io import read_frame
import kkkk
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
########### MLA EMAIL Sendiing ###################
class mlaemailsent(APIView):
    def get(self, request):
        output = BytesIO()
        data = la.objects.all()
        sendstatus = []
        for i in data :
            print(i.Email_address)
            try :
                send_mail(
                    # title:
                    "Account",
                    # message:
                    "Email Working",
                    # from:
                    'adhikar869@gmail.com',
                    # to:
                    ['kathi.mohangoud@gmail.com',]
                )
                sendstatus.append('sent')
            except :
                sendstatus.append('Not sent')
        qs = la.objects.all()
        df = read_frame(qs)
        df['sendstatus'] = sendstatus
        del df["id"]
        df.to_excel(output)
        response = HttpResponse(content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename="output.xlsx"'
        response.write(output.getvalue())
        '''for i in data :
            print(i.MLA_name)
            print(i.Email_address)
        return Response({'msg':'ok'})'''
        return response
'''class mlaemailsent(generics.ListAPIView):
    serializer_class =  Legislative_AssemblySerializers1
    def get_queryset(self,request):
        s = request.data['state']
        print(s)
        return Legislative_Assembly1.objects.filter(state=s)'''
def export11(request):
    la = Legislative_Assembly1.objects.filter(state=39)
    return JsonResponse({'status':200})
class ExportImportExcelView(APIView):
    def get(self,request):
        #m = request.GET.get('k')
        Legislative_Assembly1_objs =Legislative_Assembly1.objects.filter(state=10)
        serializer = Legislative_AssemblySerializer(Legislative_Assembly1_objs,many=True)
        df = pd.DataFrame(serializer.data)
        z = df.to_dict()
        print(z)
        #excelupload.objects.create(excelfileupload = "/media/mohan/mn/mnew/m/123.xlsx")
        return Response({'k':z})
