from django.shortcuts import render
from django.http import HttpResponse

def Home(request):
    peoples = [
        {'name': 'Tajammul Latif', 'age': 24},
        {'name': 'Ahmed', 'age': 16},
        {'name': 'Muqeet', 'age': 15},
        {'name': 'Hamza', 'age': 18},
    ]
    
    vegetables = ['pumpkins', 'potato', 'tomato', 'cucumber']
    return render(request, 'home/index.html', context = {'peoples': peoples, 'vegetables': vegetables})


def success_page(request):
    return HttpResponse("<h1>Hey, This is a Success Page</h1>")