from rest_framework import viewsets
from .serializers import MovieSerializer, StillSerializer
from .models import Movie, Still


class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class StillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Still.objects.all()
    serializer_class = StillSerializer


class DirectorViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MovieSerializer

    def get_queryset(self):
        director_name = self.request.query_params.get('director_name', None)
        if director_name is not None:
            return Movie.objects.filter(director__icontains=director_name)
        return Movie.objects.none()
