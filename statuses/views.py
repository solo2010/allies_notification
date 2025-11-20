from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Status

def show(request):
    statuses = Status.objects.all().values()
    template = loader.get_template('statuses/show.html')
    context = {
        'statuses': statuses
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
