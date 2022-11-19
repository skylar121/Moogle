"""final_pjt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    # 전체 영화 페이지 ( home )
    path('',views.movie_list),
    # 단일 영화 조회
    path('<int:id>/',views.movie_detail),
    
    # 데이터 불러오기
    path('get_movie/',views.get_movie),
    path('get_genre/',views.get_genre),
    path('goto_main/',views.goto_main),
    path('action10/',views.action10),
    
    #drf-spectacular
    path('schema/', SpectacularAPIView.as_view(),name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'),name='swagger-ui'),
    # -------------------------------------------------------
    path('community_list_create/', views.community_list_create), # 게시글 작성을 위한
    path('community/<int:community_pk>/', views.community_update_delete),

    path('comments/<int:community_pk>/', views.comment_list),
    path('<int:community_pk>/comment/', views.create_comment),
    path('comment/<int:community_pk>/<int:comment_pk>/', views.comment_delete),

    
    path('<int:movie_pk>/review_list_create/', views.review_list_create), # 리뷰 게시글 작성을 위한
    # path('review_detail/<int:review_pk>/', views.review_detail),
    path('review/<int:review_pk>/', views.review_update_delete),

    path('review_comments/<int:review_pk>/', views.review_comment_list),
    path('<int:review_pk>/review_comment/', views.create_review_comment),
    path('review_comment/<int:review_pk>/<int:review_comment_pk>/', views.review_comment_delete),

    path('recommend/', views.recommend),
    path('<int:my_pk>/<movie_title>/like/', views.movie_like),
    path('<int:my_pk>/like/', views.my_movie_like),
    path('<int:my_pk>/like/users/', views.like_movie_users),
    # -----------------------------------------------------------
    # path('action20/',views.action20),
]
