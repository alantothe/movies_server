from rest_framework import viewsets
from .serializers import MovieSerializer, StillSerializer
from .models import Movie, Still


class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class StillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Still.objects.all()
    serializer_class = StillSerializer
