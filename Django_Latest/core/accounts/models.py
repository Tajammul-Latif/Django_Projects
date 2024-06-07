from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from .manager import *

# Create your models here.

class CustomUser(AbstractBaseUser):
    username = None
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(unique=True)
    user_bio = models.CharField(max_length=100)
    user_profile_image = models.ImageField(upload_to='profile')
    
    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()
    
    