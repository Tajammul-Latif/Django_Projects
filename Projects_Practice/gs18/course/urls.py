from django.urls import path
from course import views

urlpatterns = [
     path('course-info/', views.showCourseInfo, name='course_info')
]
