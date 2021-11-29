from rest_framework.utils import serializer_helpers
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication
from rest_framework import status
from api.models import Genre

from core.models import Movie, User
from api.models import Review
from api.serializers import GenreSerializer, MovieDetailsSerializer, ReviewSerializer, UserSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated


class MovieViewSet(viewsets.ModelViewSet):
    serializer_class = MovieDetailsSerializer    
    permission_classes = [] #disables permission for public api

    def get_queryset(self, *args, **kwargs):
        choice_tuple = (
            'release_date',
            'upvotes',
            'downvotes'
        )

        sort_by_filter = self.request.query_params.get('sort_by')
        if sort_by_filter in choice_tuple:
            qs = Movie.objects.all().order_by(sort_by_filter)
            return qs

class GenreViewSet(viewsets.ModelViewSet):
    serializer_class = GenreSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self, *args, **kwargs):
        if self.request.user.favourite_genre:
            queryset = Genre.objects.filter(name=self.request.user.favourite_genre)
            return queryset


class UserviewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return super().update(request, *args, **kwargs)

class ReviewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer