from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import MovieViewSet, StillViewSet

router = routers.DefaultRouter()
router.register('movies', MovieViewSet)
router.register('stills', StillViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
#     path('admin/', admin.site.urls)
# ]
