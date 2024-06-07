from django.contrib import admin
from myApp.models import ImageUpload

# Register your models here.
@admin.register(ImageUpload)
class ImageUploadAdmin(admin.ModelAdmin):
    list_display = ['id', 'photo', 'date']
    
    

