from core.models import Movie
from api.models import Genre, Review
from rest_framework import serializers 
from core.models import *


class MoviesSerializer(serializers.ModelSerializer):
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all(), required=False)
    reviews = serializers.RelatedField(queryset=Review.objects.all(), required=False) 
    class Meta:
        model = Movie
        fields = ['name', 'genre', 'release_date', 'upvotes', 'downvotes', 'reviews']


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = '__all__'

class GenreSerializer(serializers.ModelSerializer):
    recommendation = serializers.SerializerMethodField()

    class Meta:
        model = Genre
        fields = ['recommendation', ]
    
    def get_recommendation(self, instance):
        movie_instances = Movie.objects.filter(genre=instance)
        if movie_instances.exists():
            return MovieSerializer(movie_instances, many=True).data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class MoviewReviewAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',)


class MoviewReviewSerializer(serializers.ModelSerializer):
    author = MoviewReviewAuthorSerializer(many=False, read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'body', 'author')


class MovieDetailsSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ('id', 'name', 'genre', 'release_date', 'reviews')

    def get_reviews(self, obj):
        reviews = obj.reviews.all().order_by('-creation_time')
        # select all author links in one query
        return MoviewReviewSerializer(
            reviews.select_related('author'), many=True).data