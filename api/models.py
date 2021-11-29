# from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
class Review(models.Model):
    body = models.CharField(max_length=250)
    movie = models.ForeignKey('core.Movie', on_delete=models.CASCADE, 
                               related_name='reviews')
    author = models.ForeignKey('core.User', on_delete=models.CASCADE,
                               related_name='reviews')
    creation_time = models.DateTimeField(default=timezone.now(), editable=False)

    def __str__(self):
        return self.body
        
class Genre(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

