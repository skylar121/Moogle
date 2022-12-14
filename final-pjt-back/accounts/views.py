from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import User
from .serializers import UserSerializer
# Create your views here.


# def some_view_func(request):
#     token = Token.objects.create(user=...)
#     return Response({'token':token.key})


User = get_user_model()



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_info(request, username):
    person = get_object_or_404(User, username=username)
    serializer = UserSerializer(person)
    return Response(serializer.data)




# def user_follow(request, username):
#     follow_user = get_object_or_404(User, username=username, is_active=True)

#     request.user.following_set.add(follow_user)
#     follow_user.follower_set.add(request.user)

#     messages.success(request, f'{follow}')







# def follow(self, request, user_id):
#         # user가 2가지 있어서 혼동 방지를 위해 
#         you = get_object_or_404(User, id=user_id)
#         me = request.user
#         if me in you.follow.all(): # users/models.py의 related_name=followers
#             you.follow.remove(me) # (request.user)
#             return Response("언팔로우 했습니다.", status=status.HTTP_200_OK)
#         else:
#             you.follow.add(me) # 너의 팔로워에 나를 더해라
#             return Response("팔로우 했습니다.", status=status.HTTP_200_OK)



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


from django.http import JsonResponse , HttpResponse


# 팔로우, 언팔로우
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def follow(request, username):
    # person = User.objects.get(pk=user_pk)
    person = get_object_or_404(User, username=username)
    print(person)
    user = request.user
    print(user)
    # follow하려는 대상이 사용자가 아닐때만 가능
    if person != user:
        if person.followers.filter(pk=user.pk).exists():
            person.followers.remove(user)
            is_follow = False
        else:
            person.followers.add(user)
            is_follow = True
        res = {
            'is_follow': is_follow,
            'followers': person.followers.count(),
            'followings': person.followings.count(),
        }
        return JsonResponse(res)
    return HttpResponse(status=200)

# 팔로워 값
@api_view(['GET'])
def followers_list(request, username):
    person = get_object_or_404(User, username=username)
    followerslist = person.followers.all()
    serializer = UserSerializer(followerslist, many=True)
    return Response(serializer.data)

# 팔로잉 값
@api_view(['GET'])
def followings_list(request, username):
    person = get_object_or_404(User, username=username)
    followingslist = person.followings.all()
    serializer = UserSerializer(followingslist, many=True)
    return Response(serializer.data)


def post_img(request,user_pk):
    user = get_object_or_404(User, pk=user_pk)
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(user)
    img = User.objects.get('profile_img')
    
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print(img)
    return Response(img)
    