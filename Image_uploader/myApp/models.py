from django.db import models

# Create your models here.

class ImageUpload(models.Model):
    photo = models.ImageField(upload_to="MyImage")
    date = models.DateField(auto_now_add=True)
