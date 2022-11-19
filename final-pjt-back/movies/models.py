from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()


class Movie(models.Model):
    title = models.TextField()
    overview = models.TextField()
    genres = models.ManyToManyField(Genre)
    release_date = models.TextField(null=True)
    id = models.IntegerField(primary_key=True)
    adult = models.BooleanField()
    popularity = models.FloatField()
    vote_average = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    vote_count = models.IntegerField()
    poster_path = models.TextField(null=True)
    backdrop_path = models.TextField(null=True)
