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
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from . import views

urlpatterns = [
    # path('follow/<username>/',views.follow, name='follow'),
    # path('<username>/followers/',views.followers_list, name='followers'),
    # path('<username>/followings/',views.followings_list, name='followings'),
    path('<int:user_pk>/post_img/',views.post_img),
    # path('profile/<username>/',views.profile, name='profile'),
    # path('get_movie/',views.get_movie)
    # path('follow/<str:username>/'),
]
