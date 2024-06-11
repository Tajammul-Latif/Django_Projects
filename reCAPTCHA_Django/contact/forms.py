from django import forms
from django_recaptcha.fields import ReCaptchaField
from django_recaptcha.widgets import ReCaptchaV2Checkbox 

class ContactForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    feedback = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control'}))
    captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox) 