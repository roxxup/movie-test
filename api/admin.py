from django.contrib import admin
from api.models import Genre, Review
from core.models import Movie, User

# Register your models here.
admin.site.register(Movie)
admin.site.register(Genre)
admin.site.register(User)
admin.site.register(Review)