from django.urls import path, re_path
from rest_framework import routers
from .views import MovieViewSet, StillViewSet, DirectorViewSet
from .views import GenreViewSet, CountryViewSet, EmptyViewSet

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)
router.register('stills', StillViewSet)

urlpatterns = [
    path('directors/<str:director_name>/',
         DirectorViewSet.as_view({'get': 'list'}), name='director-movies'),
    path('genres/<str:genre_name>/',
         GenreViewSet.as_view({'get': 'list'}), name='genre-movies'),
    path('countries/<str:country_name>/',
         CountryViewSet.as_view({'get': 'list'}), name='country-movies'),
    re_path(r'^directors/$',
            EmptyViewSet.as_view({'get': 'list'}), name='empty-director-list'),
    re_path(r'^genres/$',
            EmptyViewSet.as_view({'get': 'list'}), name='empty-genre-list'),
    re_path(r'^countries/$',
            EmptyViewSet.as_view({'get': 'list'}), name='empty-country-list')
]
