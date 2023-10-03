from django.contrib import admin
from django.urls import path
from rest_framework import routers
from .views import MovieViewSet, StillViewSet, DirectorViewSet, GenreViewSet, CountryViewSet

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)
router.register('stills', StillViewSet)

urlpatterns = [
    path('directors/<str:director_name>/',
         DirectorViewSet.as_view({'get': 'list'}), name='director-movies'),
    path('genres/<str:genre_name>/',
         GenreViewSet.as_view({'get': 'list'}), name='genre-movies'),
    path('countries/<str:country_name>/',
         CountryViewSet.as_view({'get': 'list'}), name='country-movies')
]
