from django.core.management.base import BaseCommand
from movies.models import Movie, Still
import json


class Command(BaseCommand):
    help = 'Seed database'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str,
                            help='Path to the JSON file')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']

        with open('your_data.json', 'r') as file:
            data = json.load(file)

        movie_data = {
            'title': data['title'],
            'date_released': data['date_released'],
            'genre': data['genre'],
            'rating': data['rating'],
            'director': data['director'],
            'country': data['country'],
            'imdb_rating': data['imdb_rating'],
            'imdb_id': data['imdb_id'],
        }

        movie_instance = Movie(**movie_data)
        movie_instance.save()

        stills_data = data['stills']
        imdb_id = data['imdb_id']

        for image_url in stills_data:
            still_data = {
                'imdb_id': imdb_id,
                'image_url': image_url,
            }
            still_instance = Still(**still_data)
            still_instance.save()
