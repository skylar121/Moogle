from rest_framework import serializers
from .models import Movie, Genre, Community, Comment, Review, ReviewComment

class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = '__all__'
        read_only_fields = ('genre',)

class MovieListSerializer(serializers.ModelSerializer):
    # genres = GenreSerializer(many=True, read_only=True)
    # genre_name = serializers.CharField(source='genres.name')
    class Meta:
        model = Movie
        fields = '__all__'


# title, poster , backdrop, vote_average
class MovieDetailSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True, read_only=True)
    class Meta:
        model = Movie
        fields = '__all__'

# ------------------------------------------------------
class CommunityListSerializer(serializers.ModelSerializer):
  userName = serializers.SerializerMethodField()
  
  def get_userName(self,obj):
    return obj.user.username

  class Meta:
    model = Community
    fields = ('id', 'userName', 'user', 'title', 'content', 'created_at', 'updated_at',)
    read_only_fields = ('user',)


class CommentSerializer(serializers.ModelSerializer):
  userName = serializers.SerializerMethodField()
  
  def get_userName(self,obj):
    return obj.user.username

  class Meta:
    model = Comment
    fields = ('id', 'userName', 'user', 'content', 'created_at', 'updated_at', 'community',)
    read_only_fields = ('user','community',)
    
class ReviewListSerializer(serializers.ModelSerializer):
  movie_title = serializers.SerializerMethodField()

  def get_movie_title(self, obj):
    return obj.movie.title

  userName = serializers.SerializerMethodField()
  
  def get_userName(self,obj):
    return obj.user.username

  class Meta:
    model = Review
    fields = ('id', 'user', 'userName', 'title', 'content', 'movie', 'rank', 'created_at', 'updated_at', 'movie_title')
    read_only_fields = ('user', 'movie')


class ReviewCommentSerializer(serializers.ModelSerializer):
  userName = serializers.SerializerMethodField()
  
  def get_userName(self,obj):
    return obj.user.username

  class Meta:
    model = ReviewComment
    fields = ('id', 'userName', 'user', 'content', 'review', 'rank', 'created_at', 'updated_at',)
    read_only_fields = ('user', 'review',)