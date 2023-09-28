from django.db import models


class Movie(models.Model):
    title = models.CharField()
    date_released = models.DateField()
    genre = models.CharField()
    rating = models.CharField()
    director = models.CharField()
    country = models.CharField()
    imdb_rating = models.FloatField()
    imdb_id = models.CharField()

    def __str__(self):
        return self.title
