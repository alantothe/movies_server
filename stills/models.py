from django.db import models
from movies.models import Movie


class Still(models.Model):
    image_url = models.CharField()
    movie_id = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='stills'
    )

    def __str__(self):
        return self.image_url
