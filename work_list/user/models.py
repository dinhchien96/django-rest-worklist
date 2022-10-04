from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager


# Create your models here.
class User(AbstractBaseUser):
    user_id = models.AutoField(primary_key=True, db_index=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    refresh_token = models.CharField(max_length=1000, blank=True, null=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    USER_ID_FIELD = 'user_id'
    REQUIRED_FIELDS = []
    
