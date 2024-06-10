from django.db import models

class saveFormData(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    websiteLink = models.CharField(max_length=70)
    message = models.TextField()

# Create your models here.
