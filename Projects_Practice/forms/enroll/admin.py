from django.contrib import admin
from enroll.models import Contact

# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'message']
