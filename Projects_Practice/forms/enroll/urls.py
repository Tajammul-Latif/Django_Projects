from django.urls import path, include
from enroll import views

urlpatterns = [
    path('', views.Contact_View),
]
