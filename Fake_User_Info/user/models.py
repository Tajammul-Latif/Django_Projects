from django.db import models

# Register your models here.
class User(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    user_email = models.EmailField(unique=True)
