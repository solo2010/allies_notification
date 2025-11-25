from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import PartnerGroup, PartnerGroupProduct
from products.models import Product
from .forms import PartnerGroupForm

def show(request):
    partner_groups = PartnerGroup.objects.all().values()
    template = loader.get_template('partner_groups/show.html')
    context = {
        'partner_groups': partner_groups
    }
    return HttpResponse(template.render(context))

def create(request):
    
    if request.method == "POST":
        form = PartnerGroupForm(request.POST)
        if form.is_valid():
            name = request.POST.get("name")
            product = Product.objects.get(id=request.POST.get("product"))
            partnergroup = PartnerGroup.objects.create(name=name)
            PartnerGroupProduct.objects.create(product=product, partnergroup=partnergroup)
            return redirect("partner_groups:show")
    else:
        form = PartnerGroupForm()
        
    return render(request, "partner_groups/create.html", {"form": form})

def delete(request,id):
    partner_group = PartnerGroup.objects.get(id=id)
    partner_group.delete()
    return redirect("partner_groups:show")

def edit(request,id):
    partner_group = PartnerGroup.objects.get(id=id)
    if request.method == "POST":
        form = PartnerGroupForm(request.POST)
        if form.is_valid():
            partner_group.name = request.POST['name']
            partner_group.save()
            return redirect("partner_groups:show")
    else:
        form = PartnerGroupForm(initial={
            'name': partner_group.name
        })
    
    return render(request, "partner_groups/edit.html", {"form": form})





