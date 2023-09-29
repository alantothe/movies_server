from django.db import models


class Movie(models.Model):
    imdb_id = models.CharField(max_length=20, primary_key=True)
    title = models.CharField(max_length=255)
    date_released = models.DateField()
    genre = models.JSONField()
    rating = models.CharField(max_length=10)
    director = models.JSONField()
    country = models.JSONField()
    imdb_rating = models.DecimalField(max_digits=3, decimal_places=1)


class Still(models.Model):
    imdb_id = models.CharField(max_length=20)
    image_url = models.CharField(max_length=1000)
