from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from . serializers import MovieSerializer
from . serializers import BiharCandidateSerializers
from . serializers import DubbakaCandidateSerializers
from . models import Movie
from . models import BiharCandidate
from . models import DubbakaCandidate
from rest_framework.views import APIView
from rest_framework.response import Response


class MovieViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    #permission_classes = [permissions.IsAuthenticated]
    '''def list(self, request, *args, **kwargs):
        movies = Movie.objects.all()
        serializer = MovieMiniSerializer(movies, many=True)
        return Response(serializer.data)'''

class Bihar_api(APIView):
    def get(self,request):
        data = BiharCandidate.objects.all()
        serializer = BiharCandidateSerializers(data, many=True)
        return Response(serializer.data)

class Dubbaka_api(APIView):
    def get(self,request):
        data = DubbakaCandidate.objects.all()
        serializer = DubbakaCandidateSerializers(data, many=True)
        return Response(serializer.data)

