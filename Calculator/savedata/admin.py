from django.contrib import admin
from savedata.models import saveFormData

class SaveDataAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'websiteLink', 'message')
    
admin.site.register(saveFormData, SaveDataAdmin)

# Register your models here.


# Register your models here.
