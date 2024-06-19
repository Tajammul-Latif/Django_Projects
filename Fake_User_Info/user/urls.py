from django.urls import path
from user.views import *

urlpatterns = [
    path('', userInfo, name='user-info')
]
