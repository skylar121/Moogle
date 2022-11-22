from rest_framework import serializers
from dj_rest_auth.registration.serializers import RegisterSerializer

from .models import User
class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField()
    profile_image = serializers.ImageField(use_url=True, required=False)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        # print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        
        data['nickname'] = self.validated_data['nickname']
        data['profile_image'] = self.validated_data['profile_image']


        return data

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ('id', 'username', 'email', 'nickname', 'profile_image',)
        # read_only_fields = '__all__'