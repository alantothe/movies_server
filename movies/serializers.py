from rest_framework import serializers
from .models import Movie, Still


class MovieSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Movie
        fields = [f.name for f in Movie._meta.fields] + ['stills']


class StillSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Still
        fields = '__all__'
