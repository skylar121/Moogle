from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    followers = models.ManyToManyField('self',symmetrical=False, related_name='followings')
    # users = models.CharField(max_length=50)
    # password = models.CharField(max_length=50)
    # followers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followings')
    nickname = models.CharField(max_length=50)
    # gender = models.SmallIntegerField()
    profile_image = models.ImageField(upload_to='users', blank=True)
    pass
