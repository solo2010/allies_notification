from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .forms import ProductForm
from .models import Product
from django.urls import reverse


def show(request):
    products = Product.objects.all().values()
    template = loader.get_template('products/show.html')
    context = {
        'products': products
    }
    return HttpResponse(template.render(context, request))

def create(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            name = request.POST.get("name")
            Product.objects.create(name=name)
            return redirect("products:show")
    else:
        form = ProductForm()
    
    return render(request, "products/create.html", {"form": form})

def delete(request, id):
    product = Product.objects.get(id=id)
    product.delete()
    return redirect("products:show")

def edit(request, id):
    product = Product.objects.get(id=id)
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            product.name = request.POST['name']
            product.save()
            return redirect("products:show")
    else:
        form = ProductForm(initial={
            'name': product.name
        })
    
    return render(request, "products/edit.html", {"form": form})

