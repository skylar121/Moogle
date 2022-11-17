from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    # users = models.CharField(max_length=16)
    # password = models.CharField(max_length=20)
    # profile_image = models.ImageField(upload_to='users', null=True)

    pass    