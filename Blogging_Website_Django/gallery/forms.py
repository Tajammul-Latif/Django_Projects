from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_name', 'product_description', 'product_image']
        widgets = {
            'product_name': forms.TextInput(attrs={'class': 'form-control'}),
            'product_description': forms.Textarea(attrs={'class': 'form-control'}),
            'product_image': forms.ClearableFileInput(attrs={'class': 'img-fluid'}),
        }
        
