from .models import *
from .serializers import *
from rest_framework import viewsets
class flagViewset(viewsets.ModelViewSet):
    queryset = flag.objects.all()
    serializer_class = flagSerializers
