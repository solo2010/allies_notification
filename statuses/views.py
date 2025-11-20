from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from .models import Status
from .forms import StatusForm

def show(request):
    statuses = Status.objects.all().values()
    template = loader.get_template('statuses/show.html')
    context = {
        'statuses': statuses
    }
    return HttpResponse(template.render(context, request))

def create(request):
    if request.method == "POST":
        form = StatusForm(request.POST)
        if form.is_valid():
            status = request.POST.get("status")
            Status.objects.create(status=status)
            return redirect("statuses:show")
    else:
        form = StatusForm()

    return render(request, "statuses/create.html", {"form": form})

def delete(request, id):
    status = Status.objects.get(id=id)
    status.delete()
    return redirect("statuses:show")

def edit(request, id):
    status = Status.objects.get(id=id)
    if request.method == "POST":
        form = StatusForm(request.POST)
        if form.is_valid():
            status.status = request.POST['status']
            status.save()
            return redirect("statuses:show")
    else:
        form = StatusForm(initial={
            'status': status.status
        })

    return render(request, "statuses/edit.html", {"form": form})
