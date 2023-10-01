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

        with open(json_file, 'r') as file:
            data = json.load(file)

        for item in data:  # Loop through the list of movie objects
            movie_data = {
                'title': item['title'],
                'date_released': item['date_released'][:10],
                # Since genre is a list, you might want to join it into a string
                'genre': ', '.join(item['genre']),
                'rating': item['rating'],
                'director': ', '.join(item['director']),  # Same with director
                'country': ', '.join(item['country']),  # Same with country
                'imdb_rating': item['imdb_rating'],
                'imdb_id': item['imdb_id'],
            }

            movie_instance = Movie(**movie_data)
            movie_instance.save()

            stills_data = item['stills']
            imdb_id = item['imdb_id']

            for image_url in stills_data:
                still_data = {
                    'imdb_id': movie_instance,
                    'image_url': image_url,
                }
                still_instance = Still(**still_data)
                still_instance.save()
