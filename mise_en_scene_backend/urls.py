from django.contrib import admin
from django.urls import path, include
from movies.urls import router as movie_router
from movies.urls import urlpatterns as movie_urlpatterns
from movies.urls import single_field_url_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(movie_router.urls)),
    path('', include(movie_urlpatterns)),
    path('only/', include(single_field_url_patterns))
]
