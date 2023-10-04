from rest_framework import viewsets
from rest_framework.response import Response
from .serializers import MovieSerializer, StillSerializer
from .serializers import DirectorOnlySerializer, TitleOnlySerializer
from .serializers import GenreOnlySerializer, CountryOnlySerializer
from .models import Movie, Still


class MovieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class StillViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Still.objects.all()
    serializer_class = StillSerializer


class TitleViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MovieSerializer

    def get_queryset(self):
        title_name = self.kwargs['title_name']
        return Movie.objects.filter(title__icontains=title_name)


class DirectorViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MovieSerializer

    def get_queryset(self):
        director_name = self.kwargs['director_name']
        return Movie.objects.filter(director__icontains=director_name)


class GenreViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MovieSerializer

    def get_queryset(self):
        genre_name = self.kwargs['genre_name']
        return Movie.objects.filter(genre__icontains=genre_name)


class CountryViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MovieSerializer

    def get_queryset(self):
        country_name = self.kwargs['country_name']
        return Movie.objects.filter(country__icontains=country_name)


class YearViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MovieSerializer

    def get_queryset(self):
        year_number = self.kwargs['year_number']
        return Movie.objects.filter(date_released__year=year_number)


class EmptyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = MovieSerializer
    queryset = Movie.objects.none()


class DirectorOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = DirectorOnlySerializer

    def get_queryset(self):
        distinct_directors = Movie.objects.values('director').distinct()
        return distinct_directors


class TitleOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = TitleOnlySerializer

    def get_queryset(self):
        distinct_titles = Movie.objects.values('title').distinct()
        return distinct_titles


class GenreOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = GenreOnlySerializer

    def get_queryset(self):
        distinct_genres = Movie.objects.values('genre').distinct()
        return distinct_genres


class CountryOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = CountryOnlySerializer

    def get_queryset(self):
        distinct_countries = Movie.objects.values('country').distinct()
        return distinct_countries
