from django.db import models
from django.contrib.auth.models import AbstractUser
from api.models import Review, Genre
from django.core.exceptions import ValidationError
# Create your models here.

class Movie(models.Model):
    name = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    release_date = models.DateTimeField()
    upvotes = models.PositiveIntegerField()
    downvotes = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class User(AbstractUser):
    favourite_genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)


    def __str__(self):
        return self.username