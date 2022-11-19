from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import status
import requests
import json
from .models import Movie,Genre,Community,Comment,Review,ReviewComment
from django.http import HttpResponse
from .serializer import MovieDetailSerializer, MovieListSerializer, CommunityListSerializer, CommentSerializer, ReviewListSerializer, ReviewCommentSerializer
import random


TMDB_API_KEY = 'b4e0be7fe675a0e4fdd96cca62fc6dbd'
# Create your views here.


# 전체 영화 페이지
@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)

# 단일 영화 조회
@api_view(['GET'])
def movie_detail(request,id):
    movie = get_object_or_404(Movie,id=id)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)

# 커뮤니티 리스트 생성
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def community_list_create(request):
  if request.method == 'GET':
    communities = Community.objects.all()
    serializer = CommunityListSerializer(communities, many=True)
    return Response(serializer.data)
  else:
    serializer = CommunityListSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      serializer.save(user=request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)


# 커뮤니티 단일 조회
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def community_detail(request, community_pk):
  community = get_object_or_404(Community, pk=community_pk)

  serializer = CommunityListSerializer(community)
  return Response(serializer.data)
    


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_list(request, community_pk):
    community = get_object_or_404(Community, pk=community_pk)
    comments = community.comment_set.all()
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

# 댓글 생성
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def create_comment(request, community_pk):
    community = get_object_or_404(Community, pk=community_pk)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):

        serializer.save(user=request.user, community=community)

        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 커뮤니티 게시글 삭제
@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def community_update_delete(request, community_pk):
  community = get_object_or_404(Community, pk=community_pk)

  if not request.user.communities.filter(pk=community_pk).exists():
    return Response({'message': '권한이 없습니다.'})

  if request.method == 'PUT':
      serializer = CommunityListSerializer(community, data=request.data)
      if serializer.is_valid(raise_exception=True):
          serializer.save(user=request.user)
          return Response(serializer.data)
  else:
      community.delete()
      return Response({ 'id': community_pk })

# 댓글 삭제
@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def comment_delete(request, community_pk, comment_pk):
  community = get_object_or_404(Community, pk=community_pk)
  comment = community.comment_set.get(pk=comment_pk)

  if not request.user.comments.filter(pk=comment_pk).exists():
    return Response({'message': '권한이 없습니다.'})
  else:
    comment.delete()
    return Response({ 'id': comment_pk })

# review
@api_view(['GET', 'POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_list_create(request, movie_pk):
  if request.method == 'GET':
    reviews = Review.objects.all().filter(movie_id=movie_pk)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)
  else:
    serializer = ReviewListSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
      movie = get_object_or_404(Movie, pk=request.data.get('movie'))

      pre_point = movie.vote_average * movie.vote_count
      pre_count = movie.vote_count

      point = pre_point+request.data.get('rank')
      count = movie.vote_count + 1
      new_vote_average = round(point/count, 2)

      movie.vote_average = new_vote_average
      movie.vote_count = count
      movie.save()
        
      serializer.save(user=request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)

# 리뷰 댓글 목록
@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_comment_list(request, review_pk):
  review = get_object_or_404(Review, pk=review_pk)
  comments = review.reviewcomment_set.all()
  serializer = ReviewCommentSerializer(comments, many=True)
  return Response(serializer.data)

# 리뷰 댓글 형성
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def create_review_comment(request, review_pk):
  review = get_object_or_404(Review, pk=review_pk)
  serializer = ReviewCommentSerializer(data=request.data)
  if serializer.is_valid(raise_exception=True):
    serializer.save(user=request.user, review=review)
    return Response(serializer.data, status=status.HTTP_201_CREATED)


# 리뷰 삭제
@api_view(['PUT', 'DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_update_delete(request, review_pk):
  review = get_object_or_404(Review, pk=review_pk)
  if not request.user.reviews.filter(pk=review_pk).exists():
    return Response({'message': '권한이 없습니다.'})

  if request.method == 'PUT':
    serializer = ReviewListSerializer(review, data=request.data)
    
    if serializer.is_valid(raise_exception=True):
      movie = get_object_or_404(Movie, pk=request.data.get('movie'))
      pre_point = movie.vote_average * (movie.vote_count - 1)
      pre_count = movie.vote_count - 1
      point = pre_point+request.data.get('rank')
      count = movie.vote_count
      new_vote_average = round(point/count, 2)
      movie.vote_average = new_vote_average
      movie.vote_count = count
      movie.save()
      serializer.save(user=request.user)
      return Response(serializer.data)

  else:
    review = get_object_or_404(Review, pk=review_pk)
    movie = get_object_or_404(Movie, pk=review.movie_id)
    pre_point = movie.vote_average * (movie.vote_count)
    pre_count = movie.vote_count
    point = pre_point - review.rank
    count = movie.vote_count-1
    new_vote_average = round(point/count, 2)
    movie.vote_average = new_vote_average
    movie.vote_count = count
    movie.save()
    review.delete()
    return Response({ 'id': review_pk })

# 리뷰 댓글 삭제
@api_view(['DELETE'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_comment_delete(request, review_pk, review_comment_pk):
  review = get_object_or_404(Review, pk=review_pk)
  comment = review.reviewcomment_set.get(pk=review_comment_pk)
  if not request.user.review_comments.filter(pk=review_comment_pk).exists():
    return Response({'message': '권한이 없습니다.'})

  else:
    comment.delete()
    return Response({ 'id': review_comment_pk })



@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def recommend(request):
    pass










# 영화 좋아요 ~
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_like(request, my_pk, movie_title):
  movie = get_object_or_404(Movie, title=movie_title)
  me = get_object_or_404(get_user_model(), pk=my_pk)
  if me.like_movies.filter(pk=movie.pk).exists():
      me.like_movies.remove(movie.pk)
      liking = False
      
  else:
      me.like_movies.add(movie.pk)
      liking = True
  
  return Response(liking)

# 내가 좋아요 누른 것들 내놔 !!!!!!!!!!!
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def my_movie_like(request, my_pk):
  me = get_object_or_404(get_user_model(), pk=my_pk)
  data = []
  movies = request.data
  for movie_pk in movies:
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    data.append(serializer.data)
  
  return Response(data)



# 좋아요 누른 유저 조회
@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def like_movie_users(request, my_pk):
  # print(request.data)
  users = []
  movies = request.data.get('movies')
  # print(movies)
  for movie in movies:
    movie = get_object_or_404(Movie, pk=movie)
    serializer = MovieSerializer(movie)
    # print(serializer.data)
    for user in serializer.data.get('like_users'):
      if user not in users:
        users.append(user)

  return Response(users)













# 영화 다 가져와 !
def get_movie(request):
    for i in range(1, 10):
        request_url = f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=ko-KR&page={i}"
        movies = requests.get(request_url).json()
        for movie in movies['results']:
            abc = Movie()
            abc.title = movie['title']
            abc.overview = movie['overview']
            abc.release_date = movie.get('release_date')
            abc.id = movie['id']
            abc.adult = movie['adult']
            abc.popularity = movie['popularity']
            abc.vote_average = movie['vote_average']
            abc.vote_count = movie['vote_count']
            abc.poster_path = movie['poster_path']
            abc.backdrop_path = movie['backdrop_path']
            if abc.release_date and abc.poster_path and abc.backdrop_path:
                abc.save()
                for genre in movie.get('genre_ids'):
                    abc.genres.add(genre)
    return HttpResponse()

# 장르 데이터 가져와
def get_genre(request):
    request_url = f"https://api.themoviedb.org/3/genre/movie/list?api_key={TMDB_API_KEY}&language=ko-KR"
    genres = requests.get(request_url).json()
    for genre in genres['genres']:
        jjang = Genre()
        jjang.id = genre['id']
        jjang.name = genre['name']
        jjang.save()
    return HttpResponse()

# 메인페이지 영화 쏴줄게 !
@api_view(['GET'])
def goto_main(request):
    request_url = f"https://api.themoviedb.org/3/movie/now_playing?api_key={TMDB_API_KEY}&language=ko-KR&page=1"
    movies1 = requests.get(request_url).json()
    moviejson = []
    for movie in movies1['results']:
        abc = Movie()
        abc.title = movie['title']
        abc.overview = movie['overview'] 
        abc.release_date = movie.get('release_date')
        abc.id = movie.get('id')
        abc.adult = movie['adult']
        abc.popularity = movie['popularity']
        abc.vote_average = movie['vote_average']
        abc.vote_count = movie['vote_count']
        abc.poster_path = movie['poster_path']
        abc.backdrop_path = movie['backdrop_path']
        abc.save()
        moviejson.append(abc)
        for genre in movie.get('genre_ids'):
            abc.genres.add(genre)
    else:
        serializer = MovieListSerializer(moviejson, many=True)
        return Response(serializer.data)


# 액션 영화 10개 랜덤으로 내놔 !
@api_view(['GET'])
def action10(request):
    genre = get_object_or_404(Genre, pk=28)
    movies = random.sample(list(genre.movie_set.all()[:100]),10)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)
    
    
    
    