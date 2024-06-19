from django.shortcuts import render
from user.models import User

# Create your views here.
def userInfo(request):
    users = User.objects.all().order_by('id')
    
    return render(request, 'user-info.html', context={'users': users})