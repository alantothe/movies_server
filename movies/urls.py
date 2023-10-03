from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import MovieViewSet, StillViewSet, DirectorViewSet

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)
router.register('stills', StillViewSet)
# router.register('directors',
# DirectorViewSet, basename='director')

urlpatterns = [
    path('directors/<str:director_name>/',
         DirectorViewSet.as_view({'get': 'list'}), name='director-movies')
]
