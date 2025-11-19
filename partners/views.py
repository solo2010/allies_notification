from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Partner

def show(request):
    partners =Partner.objects.all().values()
    template = loader.get_template('partners/show.html')
    context = {
        'mivariable': "hola perras",
        'partners': partners
    }
    return HttpResponse(template.render(context))

# Create your views here.
