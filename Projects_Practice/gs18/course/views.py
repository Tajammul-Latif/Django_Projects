from django.shortcuts import render

# Create your views here.

def showCourseInfo(request):
    
    return render(request, 'course/courseinfo.html')