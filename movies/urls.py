from django.urls import path, re_path
from rest_framework import routers
from .views import MovieViewSet, StillViewSet, DirectorViewSet
from .views import GenreViewSet, CountryViewSet, EmptyViewSet
from .views import TitleViewSet, YearViewSet, DirectorOnlyViewSet
from .views import TitleOnlyViewSet, GenreOnlyViewSet, CountryOnlyViewSet
from .views import YearOnlyViewSet, ImdbIdOnlyViewSet

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)
router.register('stills', StillViewSet)

single_field_url_patterns = [
    path('directors/',
         DirectorOnlyViewSet.as_view({'get': 'list'}), name='director-only'),
    path('titles/<slug:title_slug>/', 
         TitleViewSet.as_view({'get': 'list'}), name='title-movies'),
    path('genres/',
         GenreOnlyViewSet.as_view({'get': 'list'}), name='genre-only'),
    path('countries/',
         CountryOnlyViewSet.as_view({'get': 'list'}), name='country-only'),
    path('years/',
         YearOnlyViewSet.as_view({'get': 'list'}), name='year-only'),
    path('imdb/',
         ImdbIdOnlyViewSet.as_view({'get': 'list'}), name='imdb-id-only')
]

urlpatterns = [
    path('titles/<slug:title_slug>/',  
         TitleViewSet.as_view({'get': 'list'}), name='title-movies'),
    path('directors/<str:director_name>/',
         DirectorViewSet.as_view({'get': 'list'}), name='director-movies'),
    path('genres/<str:genre_name>/',
         GenreViewSet.as_view({'get': 'list'}), name='genre-movies'),
    path('countries/<str:country_name>/',
         CountryViewSet.as_view({'get': 'list'}), name='country-movies'),
    path('years/<str:year_number>/',
         YearViewSet.as_view({'get': 'list'}), name='year-movies'),
    re_path(r'^titles/$',
            EmptyViewSet.as_view({'get': 'list'}), name='empty-title-list'),
    re_path(r'^directors/$',
            EmptyViewSet.as_view({'get': 'list'}), name='empty-director-list'),
    re_path(r'^genres/$',
            EmptyViewSet.as_view({'get': 'list'}), name='empty-genre-list'),
    re_path(r'^countries/$',
            EmptyViewSet.as_view({'get': 'list'}), name='empty-country-list'),
    re_path(r'^years/$',
            EmptyViewSet.as_view({'get': 'list'}), name='empty-year-list')
]
