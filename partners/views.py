from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Partner
from .forms import PartnerForm

def show(request):
    partners =Partner.objects.all()
    print(partners)
    template = loader.get_template('partners/show.html')
    context = {
        'mivariable': "hola perras",
        'partners': partners
    }
    return HttpResponse(template.render(context))

def create(request):
    if request.method == "POST":
        form = PartnerForm(request.POST)
        if form.is_valid():
            Partner.objects.create(
                full_name = form.cleaned_data['full_name'],
                email = form.cleaned_data['email'],
                cellphone = form.cleaned_data['cellphone'],
                partner_group = form.cleaned_data['partner_group']
            )
            return redirect("partners:show")
    else:
        form = PartnerForm()
    return render(request, "partners/create.html", {"form": form})

def delete(request, id):
    print("llego acá")
    partner = Partner.objects.get(id=id)
    partner.delete()
    return redirect("partners:show")

def edit(request, id):
    partner = Partner.objects.get(id=id)
    if request.method == "POST":
        form = PartnerForm(request.POST)
        if form.is_valid():
            partner.full_name = form.cleaned_data['full_name']
            partner.email = form.cleaned_data['email']
            partner.cellphone = form.cleaned_data['cellphone']
            partner.partner_group = form.cleaned_data['partner_group']
            partner.save()
            return redirect("partners:show")
    else:
        form = PartnerForm(initial={
            'full_name': partner.full_name,
            'email': partner.email,
            'cellphone': partner.cellphone,
            'partner_group': partner.partner_group
        })

    return render(request, "partners/edit.html", {"form": form})

