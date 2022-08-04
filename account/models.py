from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=9)
    