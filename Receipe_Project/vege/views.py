from django.shortcuts import render, redirect, get_list_or_404
from .models import *
from django.db.models import Q
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Adding Reeipes in the Database
def receipes(request):
    data = request.POST
    if request.method == 'POST':
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')
        
        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image
        )
        
        return redirect('receipes')
    
    return render(request, 'receipes.html')  


# Showing Receipes 
@login_required(login_url = '/login/')
def showReceipes(request):
    queryset = Receipe.objects.all()
    
    if request.GET.get('search'):
        queryset = Receipe.objects.filter(receipe_name__icontains = request.GET.get('search'))
        
    return render(request, 'ShowReceipes.html', context={'receipes': queryset})


# Deleting Receipes 
def delete_receipe(request, id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('show_receipes')


# Updating the Receipes
def update_receipe(request, id):
    queryset = Receipe.objects.get(id = id)
    
    if request.method == 'POST':
        data = request.POST
        
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        receipe_image = request.FILES.get('receipe_image')
        
        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description
        
        if receipe_image:
            queryset.receipe_image = receipe_image
            
        queryset.save()
        return redirect('show_receipes')
    
    return render(request, 'updateReceipe.html', {'receipe': queryset})


# Login Page
def login_page(request):
    
    if request.method == 'POST':
        data = request.POST
        username = data.get('username')
        password = data.get('password')
        
        if not User.objects.filter(username = username).exists():
            messages.error(request, "User doesn't exists")
            return redirect('login_page')
        
        user = authenticate(username = username, password = password)
        
        if user is None:
            messages.error(request, 'Invalid username or password')
            return redirect('login_page')
        else:
            login(request, user)
            return redirect('show_receipes')
        
        
    return render(request, 'login.html')

# Logout Page
def logout_page(request):
    logout(request)
    return redirect('login_page')

# Registration Page
def registerPage(request):
    if request.method == 'POST':
        data = request.POST
    
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        username = data.get('username')
        password = data.get('password')
        
        user = User.objects.filter(username = username)
        
        if user.exists():
            messages.info(request, 'Username already taken')
            return redirect("register_page")
            
        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )
        
        user.set_password(password)
        user.save()
        messages.info(request, 'Account created successfully')
        return redirect('register_page')
    
    return render(request, 'register.html')