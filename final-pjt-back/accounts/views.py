from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import User
# Create your views here.


# def some_view_func(request):
#     token = Token.objects.create(user=...)
#     return Response({'token':token.key})






# def profile(request, username):
#     User =get_object_or_404(get_user_model(),username=username)

#     person = User.objects.get(username=username)

#     return Response({'username': username, })




def user_follow(request, username):
    follow_user = get_object_or_404(User, username=username, is_active=True)

    request.user.following_set.add(follow_user)
    follow_user.follower_set.add(request.user)





















# def follow(request, user_pk):
#     if request.user.is_authenticated:
#         User = get_user_model()
#         person = User.objects.get(pk=user_pk)
#         if person != request.user:
#             if person.followers.filter(pk=request.user.pk).exists():
#                 person.followers.remove(request.user)
#             else:
#                 person.followers.add(request.user)
#         return redirect('accounts:profile',person.username)
#     return redirect('accounts:login')


