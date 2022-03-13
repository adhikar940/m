from django.urls import include, path
from . views import *
from django.views.static import serve
urlpatterns = [
path('Assembly_Constituency/', Assembly_Constituency.as_view()),
path('Legislative_Assembly/', Legislative_Assembly1.as_view()),
path('assemblypersonal/', assemblypersonal1.as_view()),
path('assemblyterm/', assemblyterm.as_view()),
path('excel/',ExportImportExcelView.as_view()),
]
