from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator


class Genre(models.Model):
    tmdb_id = models.IntegerField(primary_key=True)
    name = models.TextField()


class Movie(models.Model):
    title = models.TextField()
    overview = models.TextField()
    genres = models.ManyToManyField(Genre)
    # genres = models.ManyToManyField(Genre, through="Movie_Genre_joined",through_fields=("movie_id","genre_id"),)
    release_date = models.TextField(null=True)

    tmdb_id = models.IntegerField(primary_key=True)
    
    adult = models.BooleanField()

    popularity = models.FloatField()
    vote_average = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    vote_count = models.IntegerField()
    poster_path = models.TextField(null=True)
    # youtube_key = models.TextField()
    backdrop_path = models.TextField(null=True)
# class Community(models.Model):
#     user = models.ForeignKey()

# class Movie_Genre_joined(models.Model):
#     movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
#     genre_id = models.ForeignKey(Genre, on_delete=models.CASCADE)
    
#     class Meta:
#         db_table = 'movies_movie_genres'
        