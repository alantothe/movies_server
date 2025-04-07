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
        fields = [f.name for f in Movie._meta.fields] + ['stills', 'slug']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['director'] = representation['director'].strip('"')
        representation['genre'] = representation['genre'].strip('"')
        representation['country'] = representation['country'].strip('"')
        return representation


class DirectorOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['director']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['director'] = representation['director'].strip('"')
        return representation


class TitleOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['title', 'imdb_id', 'slug']


class GenreOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['genre']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['genre'] = representation['genre'].strip('"')
        return representation


class CountryOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['country']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['country'] = representation['country'].strip('"')
        return representation


class DateOnlySerializer(serializers.Serializer):
    year = serializers.IntegerField()

    class Meta:
        model = Movie
        fields = ['date_released']


class ImdbIdOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['imdb_id']
