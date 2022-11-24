from django.shortcuts import render, get_object_or_404, get_list_or_404
from rest_framework.response import Response
from django.http import JsonResponse 
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import status
import requests
import json
from .models import Movie,Genre,Review,ReviewComment
from django.http import HttpResponse
from .serializer import MovieDetailSerializer, MovieListSerializer, ReviewListSerializer, ReviewCommentSerializer
import random
import pandas as pd 
import json
import numpy as np
from numpy.linalg import norm
from sklearn.feature_extraction.text import TfidfVectorizer
from accounts.serializers import UserSerializer

TMDB_API_KEY = 'b4e0be7fe675a0e4fdd96cca62fc6dbd'
# Create your views here.


# 전체 영화 페이지
@api_view(['GET'])
def movie_list(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie.objects.order_by('-popularity'))
        serializer = MovieListSerializer(movies, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = MovieListSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)




# 단일 영화 조회
@api_view(['GET'])
def movie_detail(request,id):
    request_url = f"https://api.themoviedb.org/3/movie/{id}?api_key={TMDB_API_KEY}&language=ko-KR"
    movie = requests.get(request_url).json()
        
    if Movie.objects.filter(pk=id).exists():
        print('yes')
        movie = get_object_or_404(Movie,pk=id)
        serializer = MovieDetailSerializer(movie)
        return Response(serializer.data)
    else:
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print(movie)
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
        if movie.get('genres'):
            for genre in movie.get('genres'):
                abc.genres.add(genre['id'])
    movie = get_object_or_404(Movie,pk=id)
    serializer = MovieDetailSerializer(movie)
    return Response(serializer.data)





# 유저 프로필
@api_view(['GET'])
def profile(request, username):
    user = get_object_or_404(get_user_model(), username=username)
    reviews = get_list_or_404(Review, user_id=user.pk)
    serializer = ReviewListSerializer(reviews, many=True)
    return Response(serializer.data)


# ----------------------------------------------------------------------

# 리뷰 생성 및 조회 (로그인 된 상태)
@api_view(['GET', 'POST'])
# @authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_list_create(request, movie_pk):
    if request.method == 'GET':
        reviews = Review.objects.all().filter(movie_id=movie_pk)
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)
    else:
        serializer = ReviewListSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            movie = get_object_or_404(Movie, pk=movie_pk)
            # pre_point = movie.vote_average * movie.vote_count
            # point = pre_point+int(request.data.get('rank'))
            # count = movie.vote_count + 1
            # new_vote_average = round(point/count, 2)
            # movie.vote_average = new_vote_average
            # movie.vote_count = count
            # movie.save()
            
            serializer.save(user=request.user, movie=movie)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

# 리뷰 댓글 목록
@api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_comment_list(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comments = review.reviewcomment_set.all()
    serializer = ReviewCommentSerializer(comments, many=True)
    return Response(serializer.data)

# 리뷰 댓글 형성
@api_view(['POST'])
# @authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def create_review_comment(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, review=review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# 리뷰 좋아요 !
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def like_toggle(request, review_pk):
    # review_id = request.GET['review_id']
    post = Review.objects.get(id=review_pk)

    if request.user.is_authenticated:
        
        user = request.user
        if post.like.filter(id=user.id).exists():
            post.like.remove(user)
            message = "좋아요 취소"
        else:
            post.like.add(user)
            message = "좋아요"
        context = {'like_count' : post.like.count(), "message":message}
        return JsonResponse(context)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def like_count(request, review_pk):
    post = Review.objects.get(id=review_pk)
    serializer = ReviewListSerializer(post)
    return Response(serializer.data)

# 리뷰 삭제
@api_view(['PUT', 'DELETE'])
# @authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_update_delete(request, review_pk):
    print('YES')
    review = get_object_or_404(Review, pk=review_pk)
    
    if not request.user.reviews.filter(pk=review_pk).exists():
        return Response({'message': '권한이 없습니다.'})

    if request.method == 'PUT':
        serializer = ReviewListSerializer(review, data=request.data)
        print('YES')
        if serializer.is_valid(raise_exception=True):
            # movie = get_object_or_404(Movie, pk=review.movie)
            # pre_point = movie.vote_average * (movie.vote_count - 1)
            # pre_count = movie.vote_count - 1
            # point = pre_point+request.data.get('rank')
            # count = movie.vote_count
            # new_vote_average = round(point/count, 2)
            # movie.vote_average = new_vote_average
            # movie.vote_count = count
            # movie.save()
            serializer.save(user=request.user)
            return Response(serializer.data)

    else:
        review = get_object_or_404(Review, pk=review_pk)
        movie = get_object_or_404(Movie, pk=review.movie_id)
        # pre_point = movie.vote_average * (movie.vote_count)
        # pre_count = movie.vote_count
        # point = pre_point - review.rank
        # count = movie.vote_count-1
        # new_vote_average = round(point/count, 2)
        # movie.vote_average = new_vote_average
        # movie.vote_count = count
        # movie.save()
        review.delete()
        return Response({ 'id': review_pk })

# 리뷰 댓글 삭제
@api_view(['DELETE'])
# @authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def review_comment_delete(request, review_pk, review_comment_pk):
    review = get_object_or_404(Review, pk=review_pk)
    comment = review.reviewcomment_set.get(pk=review_comment_pk)
    if not request.user.review_comments.filter(pk=review_comment_pk).exists():
        return Response({'message': '권한이 없습니다.'})

    else:
        comment.delete()
        return Response({ 'id': review_comment_pk })

#

# 좋아요 기반 추천 !!!!!!
@api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
# @permission_classes([IsAuthenticated])
def recommend(request,user_pk):
    print(request)
    file_path = "movies/fixtures/movies.json"

    with open(file_path, 'r', encoding="UTF-8") as f:
        data = json.load(f)
    new_data = []
    for d in data:
        new_data.append({
            'pk': d['pk'],
            'adult': d['fields']['adult'],
            'overview': d['fields']['overview'],
            'title': d['fields']['title'],
            'poster_path': d['fields']['poster_path'],
            'genres': d['fields']['genres'],
            'vote_average': d['fields']['vote_average'],
        })

    new_data = pd.DataFrame(new_data)

    # print(new_data)
    #데이터가 많은 관계로 20000개까지 짜름 

    # sys.stdout.close()

    new_data['overview'].isnull().sum() #135
    new_data['overview']=new_data['overview'].fillna('')
    new_data['overview'].isnull().sum() #0 으로 바뀜 내적하면 모두 0 나옴 
    # print(new_data['overview'])
    # print('111111111111')

    tfidf=TfidfVectorizer(stop_words='english')#불용어 제거
    # print(type(tfidf))
    tfidf_mat=tfidf.fit_transform(new_data['overview']).toarray()

    def cos_sim2(X,Y):
        return np.dot(X,Y)/((norm(X)*norm(Y))+1e-7)

    # print(new_data['title'])
    # print(new_data['original_title'][10])
    def top_match_ar2(new_data, name, rank=5,simf=cos_sim2):
        sim=[]
        for i in range(len(new_data)):
            if name != i:
                sim.append((simf(new_data[i],new_data[name]),i))
        sim.sort()
        sim.reverse()
        return sim[:rank]

#     

#     # 유저가 좋아요 한 영화 넘겨 받기 ( 3개 )
    
    user = get_object_or_404(get_user_model(),pk = user_pk)
    # print(user)
    lst1 = list(user.like_movies.all().values())                            # 좋아요 누른 영화 리스트
    
    lst = []                                                                # 새로운 리스트
    movieList = []

    if len(lst1) >= 3:                      # 좋아요를 누른 영화가 3개 이상일 경우
        for elt in lst1:
            lst.append(elt['title'])
        print(movieList)
    else:                                   # 좋아요를 누른 영화가 3개 미만일 경우
        lst1.append(list(Movie.objects.all().values),3 )
        for elt in lst1:
            lst.append(elt['title'])                        
        
        print(lst) 
    movieList = random.sample(lst,3)
    # print(user.movie_set.all())

#     # 좋아요 한 영화의 리스트를 for문 돌려서
#     # 영화 이름마다 밑에 함수를 돌려주기
#     # 최종적으로 영화 추천 리스트가 담긴 recommend_lst 넘겨주기  
    recommend_lst = set()
    res_list = []
    for movie_name in movieList:

    #     movie_name = '돈 리브'
    #     # 여기에 영화 이름 동적으로 할당
    #     # movie_name = 영화 이름
        movie_idx = list(new_data['title']).index(movie_name)
#   print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        for sim, movie_id in top_match_ar2(tfidf_mat, movie_idx ,20):
            # res_list.append((new_data.loc[movie_id,'pk'], new_data.loc[movie_id,'title'], new_data.loc[movie_id,'poster_path']))
            res_list.append(str({'id': new_data.loc[movie_id,'pk'], 'title' :new_data.loc[movie_id,'title'], 'poster_path' :new_data.loc[movie_id,'poster_path'], 'vote_average' :new_data.loc[movie_id,'vote_average']}))
            # print({'id': new_data.loc[movie_id,'pk'], 'title' :new_data.loc[movie_id,'title'], 'poster_path' :new_data.loc[movie_id,'poster_path']})
        for res in res_list[:30]:
            recommend_lst.add(res)
    result = []
    for i in recommend_lst:
        i = eval(i)
        result.append(i)
        # i = i.lstrip('\'')

    #     return Response(recommend_lst)
    #     # print(movieList[:10])
    # print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    # print(recommend_lst)
    # print(recommend_lst)
    return Response(result)

#_______________________________________________________________________________________________________________________________________________________________________



# 영화 좋아요 ~
@api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def movie_like(request, my_pk, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    me = get_object_or_404(get_user_model(), pk=my_pk)
    if me.like_movies.filter(pk=movie.pk).exists():
        me.like_movies.remove(movie.pk)
        liking = False
        
    else:
        me.like_movies.add(movie.pk)
        liking = True
    
    return Response(liking)

# 유저가 좋아요 누른 영화 조회
@api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def my_movie_like(request, my_pk):
    me = get_object_or_404(get_user_model(), pk=my_pk)
    movies = me.like_movies.all()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

    # data = []

    # movies = request.data
    # for movie_pk in movies:
    #     movie = get_object_or_404(Movie, pk=movie_pk)
    #     serializer = MovieListSerializer(movie)
    #     data.append(serializer.data)
    
    # return Response(data)



# 영화 좋아요 누른 유저 조회
@api_view(['GET'])
# @authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def like_movie_users(request, movie_pk):
    # print(request.data)
    movie = get_object_or_404(Movie, pk=movie_pk)
    users = movie.like_users.all()
    serializer = UserSerializer(users, many=True)
    # print(movies)
    # for movie in movies:
    #     movie = get_object_or_404(Movie, pk=movie)
    #     serializer = MovieListSerializer(movie)
    #     # print(serializer.data)
    #     for user in serializer.data.get('like_users'):
    #         if user not in users:
    #             users.append(user)

    return Response(serializer.data)






# ----------------------------------------------------------------------------------------


# 영화 다 가져와 !
def get_movie(request):
    for i in range(1, 50):
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
                    abc.genres.add(Genre.objects.get(id=genre))
                    
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


# 액션 영화 평점 순으로 10개 내놔 !
@api_view(['GET'])
def action10(request):
    genre = get_object_or_404(Genre, pk=28)
    movies = list(genre.movie_set.order_by('-vote_average','-popularity'))
    movies = movies[0:10]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)
    
    
# 로맨스 평점 순으로 10개 내놔 !
@api_view(['GET'])
def romance10(request):
    genre = get_object_or_404(Genre, pk=10749)

    movies = list(genre.movie_set.order_by('-vote_average','-popularity'))
    movies = movies[0:10]
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)



