from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def practice_receipe(request):
    if request.method == "POST":
        data = request.POST
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_desc')
        receipe_image = request.FILES.get('receipe_image')
        
        Receipe.objects.create(
            receipe_name = receipe_name,
            receipe_description = receipe_description,
            receipe_image = receipe_image
        )
        
        return redirect('/practice_receipe')
    
    queryset = Receipe.objects.all()
    context = {'receipes': queryset}
    
    return render(request,'practice.html', context)

def practice_delete(request, id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/practice_receipe')