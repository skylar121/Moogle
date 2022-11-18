from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import status
import requests
import json
from .models import Movie,Genre
from django.http import HttpResponse
from .serializer import MovieDetailSerializer, MovieListSerializer
import random


TMDB_API_KEY = 'b4e0be7fe675a0e4fdd96cca62fc6dbd'
# Create your views here.



@api_view(['GET'])
def movie_list(request):
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request,tmdb_id):
    movie = get_object_or_404(Movie,tmdb_id=tmdb_id)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)


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
            abc.tmdb_id = movie['id']
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
        jjang.tmdb_id = genre['id']
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
        abc.tmdb_id = movie.get('id')
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
    
    
    
    