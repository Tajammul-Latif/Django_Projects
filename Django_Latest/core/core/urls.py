"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from Home.views import *
from vege.views import *
from practice_of_uploading_and_showing_query.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from emailapp.views import *

urlpatterns = [
    path('', Home, name="home"),
    path('success-page/', success_page, name="Succes-Page"),
    path('admin/', admin.site.urls),
    path('receipes/', receipes, name="receipes"),
    path('delete_receipe/<id>/', delete_receipe, name="delete_receipe"),
    path('practice_receipe/', practice_receipe, name="practice_receipe"),
    path('practice_delete/<id>', practice_delete, name="practice_delete"),
    path('update_receipe/<id>', update_receipe, name="update_receipe"),
    path('login/', loginPage, name="loginPage"),
    path('logout/', logoutPage, name="logoutPage"),
    path('register/', register, name='register'),
    path('students/', get_students, name='get_students'),
    path('marks/<student_id>/', see_marks, name='see_marks'),
    path('send-email/', send_email_view, name='send-email-view'),
    path('success/', email_sent, name='send_email'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
    
urlpatterns += staticfiles_urlpatterns()