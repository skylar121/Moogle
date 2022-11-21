from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    follow = models.ManyToManyField('self',symmetrical=False,related_name='followers')
    # users = models.CharField(max_length=50)
    # password = models.CharField(max_length=50)
    # nickname = models.CharField(max_length=50)
    # gender = models.SmallIntegerField()
    # profile_image = models.ImageField(upload_to='users', null=True)
    pass
