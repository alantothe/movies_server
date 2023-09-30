from rest_framework import viewsets
from .serializers import MovieSerializer, StillSerializer
from .models import Movie, Still
from .permissions import GETRequestsOnly


class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    permission_classes = [GETRequestsOnly]


class StillViewSet(viewsets.ModelViewSet):
    queryset = Still.objects.all()
    serializer_class = StillSerializer
    permission_classes = [GETRequestsOnly]
