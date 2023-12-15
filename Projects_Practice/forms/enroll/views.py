from django.shortcuts import render
from .forms import ContactForm
from enroll.models import Contact

# Create your views here.
def Contact_View(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            
    form = ContactForm()
    data = Contact.objects.all()
        
    return render(request, 'FormHome.html', {'form': form, 'data': data})
        
        
