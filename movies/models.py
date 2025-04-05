from django.db import models
from django.utils.text import slugify

class Movie(models.Model):
    imdb_id = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    date_released = models.DateField()
    genre = models.CharField(max_length=1000)
    rating = models.CharField(max_length=10)
    director = models.CharField(max_length=1000)
    country = models.CharField(max_length=1000)
    imdb_rating = models.DecimalField(max_digits=3, decimal_places=1)


class Still(models.Model):
    imdb_id = models.ForeignKey(
        Movie, on_delete=models.CASCADE, related_name='stills')
    image_url = models.CharField(max_length=1000)
