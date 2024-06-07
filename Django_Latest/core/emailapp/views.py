from django.shortcuts import render, redirect
from .utils import *

# Create your views here.
def email_sent(request):
    send_email_to_client()
    return render(request, 'success.html')

def send_email_view(request):
    return render(request, 'email.html')