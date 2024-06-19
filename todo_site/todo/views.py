from django.shortcuts import render, redirect
from todo.models import *
from .forms import *
from django.contrib import messages

# Create your views here.
def home(request):
    item_list = Todo.objects.order_by('-date')
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_page')
        
    form = TodoForm()
    
    page = {
        'forms': form,
        'list': item_list,
        'title': 'TODO LIST'
    }
    return render(request, 'index.html', page)

def remove(request, item_id):
    item = Todo.objects.filter(id = item_id)
    item.delete()
    messages.info(request, 'Item Removed!')
    return redirect('home_page')