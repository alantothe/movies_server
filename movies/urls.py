from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import MovieViewSet, StillViewSet, DirectorViewSet

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)
router.register('stills', StillViewSet)
router.register('directors',
                DirectorViewSet, basename='director')

# urlpatterns = [
#     path('', include(router.urls)),
#     path('admin/', admin.site.urls)
# ]
