from django.contrib import admin
from django.urls import path, include
from movies.urls import router as movie_router
from movies.urls import urlpatterns as movie_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(movie_router.urls)),
    path('', include(movie_urlpatterns))
]
