from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

def product_detail(request, pk):
    product = Product.objects.filter(pk = pk)
    return render(request, 'product_detail.html', {'product': product})

def update_product(request, pk):
    product = get_object_or_404(Product, pk = pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance=product)
    return render(request, 'update_product.html', {'form': form})

def delete_product(request, pk):
    product = get_object_or_404(Product, pk = pk)
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'delete_product.html', {'product': product})