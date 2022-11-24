from rest_framework import serializers
from .models import Movie, Genre, Review, ReviewComment
from accounts.serializers import UserSerializer
from django.contrib.auth import get_user_model


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
# class CommunityListSerializer(serializers.ModelSerializer):
#   userName = serializers.SerializerMethodField()

#   def get_userName(self,obj):
#     return obj.user.username

#   class Meta:
#     model = Community
#     fields = ('id', 'userName', 'user', 'title', 'content', 'created_at', 'updated_at',)
#     read_only_fields = ('user',)


# class CommentSerializer(serializers.ModelSerializer):
#   userName = serializers.SerializerMethodField()

#   def get_userName(self,obj):
#     return obj.user.username

#   class Meta:
#     model = Comment
#     fields = ('id', 'userName', 'user', 'content', 'created_at', 'updated_at', 'community',)
#     read_only_fields = ('user','community',)
    


# 유저 리뷰 장르 포함 영화정보 싹다 가져오는 버전
# class ReviewListSerializer(serializers.ModelSerializer):
#     movie = MovieDetailSerializer(read_only=True)
#     user = UserSerializer(read_only=True)
#     class Meta:
#         model = Review
#         fields = ('id', 'user', 'title', 'content', 'movie', 'rank', 'created_at', 'updated_at')
#         read_only_fields = ('user', 'movie')


# 유저 리뷰 장르는 없이 적당히 가져오는 버전
class ReviewListSerializer(serializers.ModelSerializer):
    movie_title = serializers.SerializerMethodField()
    movie_poster_path = serializers.SerializerMethodField()
    movie_backdrop_path = serializers.SerializerMethodField()
    # 장르는 
    # movie_genres = serializers.SerializerMethodField()

    def get_movie_title(self, obj):
        return obj.movie.title
    def get_movie_poster_path(self, obj):
        return obj.movie.poster_path
    def get_movie_backdrop_path(self, obj):
        print(obj.movie)
        return obj.movie.backdrop_path
    # def get_movie_genres(self, obj):
    #     return obj.movie.genres

    class ProfileImageSerializer(serializers.ModelSerializer):
        class Meta:
            model = get_user_model()
            fields = ('profile_image',)
            
    profile_image = ProfileImageSerializer(read_only=True)
    username = serializers.SerializerMethodField()
    nickname = serializers.SerializerMethodField()
    # profile_image = serializers.SerializerMethodField()

    def get_username(self,obj):
        return obj.user.username
    def get_nickname(self,obj):
        return obj.user.nickname
    # def get_profile_image(self,obj):
    #     return obj.user.profile_image

    class Meta:
        model = Review
        fields = ('id', 'user', 'username', 'nickname', 'profile_image', 'title', 'content', 'movie', 'rank', 'created_at', 'updated_at', 'movie_title', 'movie_poster_path', 'movie_backdrop_path', 'like')
        read_only_fields = ('user', 'movie', 'nickname', 'like')


# # 원래꺼
# # 유저 리뷰 장르는 없이 적당히 가져오는 버전
# class ReviewListSerializer(serializers.ModelSerializer):
#     movie_title = serializers.SerializerMethodField()
#     movie_poster_path = serializers.SerializerMethodField()
#     movie_backdrop_path = serializers.SerializerMethodField()
#     # 장르는 
#     # movie_genres = serializers.SerializerMethodField()

#     def get_movie_title(self, obj):
#         return obj.movie.title
#     def get_movie_poster_path(self, obj):
#         return obj.movie.poster_path
#     def get_movie_backdrop_path(self, obj):
#         print(obj.movie)
#         return obj.movie.backdrop_path
#     # def get_movie_genres(self, obj):
#     #     return obj.movie.genres

#     username = serializers.SerializerMethodField()
#     nickname = serializers.SerializerMethodField()
#     # profile_image = serializers.SerializerMethodField()

#     def get_username(self,obj):
#         return obj.user.username
#     def get_nickname(self,obj):
#         return obj.user.nickname
#     # def get_profile_image(self,obj):
#         # return obj.user.profile_image
#         # data = obj.user.profile_image.read()

#         # return HttpResponse(data, content_type=obj["ContentType"])

#     class Meta:
#         model = Review
#         fields = ('id', 'user', 'username', 'nickname', 'title', 'content', 'movie', 'rank', 'created_at', 'updated_at', 'movie_title', 'movie_poster_path', 'movie_backdrop_path', 'like')
#         read_only_fields = ('user', 'movie', 'nickname', 'like')


class ReviewCommentSerializer(serializers.ModelSerializer):
    userName = serializers.SerializerMethodField()

    def get_userName(self,obj):
        return obj.user.username

    class Meta:
        model = ReviewComment
        fields = ('id', 'userName', 'user', 'content', 'review', 'created_at', 'updated_at',)
        read_only_fields = ('user', 'review',)