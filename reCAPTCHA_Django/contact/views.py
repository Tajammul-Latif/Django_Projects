from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .forms import ContactForm

# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        
        if form.is_valid():
            return HttpResponse('Yay! you are human.')
        else:
            return HttpResponse('OOPS! Bot suspected.')
        
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})