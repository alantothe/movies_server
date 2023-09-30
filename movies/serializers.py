from rest_framework import serializers
from .models import Movie, Still


class StillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Still
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    stills = StillSerializer(many=True, read_only=True)

    class Meta:
        model = Movie
        fields = [f.name for f in Movie._meta.fields] + ['stills']
