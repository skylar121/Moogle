from django.db import models
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
# from django.contrib.postgres.fields import ArrayField
# from django.contrib.postgres.fields import ArrayField
from django.db import models

class Genre(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()

    def __str__(self):
        return self.name

class Movie(models.Model):
    title = models.TextField()
    overview = models.TextField()
    genres = models.ManyToManyField(Genre)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')
    release_date = models.TextField(null=True)
    id = models.IntegerField(primary_key=True)
    # genre_name = models.CharField(max_length=300, default=" ", blank=True)
    adult = models.BooleanField()
    popularity = models.FloatField()
    vote_average = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    vote_count = models.IntegerField()
    poster_path = models.TextField(null=True)
    backdrop_path = models.TextField(null=True)

# -------------------------------------------------------

class Community(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="communities")
  title = models.CharField(max_length=100)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="comments")
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  community = models.ForeignKey(Community, on_delete=models.CASCADE)


class Review(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="reviews")
  title = models.CharField(max_length=100)
  content = models.TextField()
  rank = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
  movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)


class ReviewComment(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="review_comments")
  content = models.TextField()
  rank = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)
  review = models.ForeignKey(Review, on_delete=models.CASCADE)
