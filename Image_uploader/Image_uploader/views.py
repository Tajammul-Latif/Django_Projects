from django.shortcuts import render
from django.http import HttpResponse
from myApp.forms import ImageForm
from myApp.models import ImageUpload


def showHomePage(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    form = ImageForm()
    image = ImageUpload.objects.all()
    
    ImageUpload.objects.all().delete()
    
    return render(request, 'index.html', {'form': form, 'image': image})