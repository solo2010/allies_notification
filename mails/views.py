from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from products.models import Product
from statuses.models import Status
from partner_groups.models import PartnerGroup
from .forms import MailForm

def show(request):
    return HttpResponse("Hola mails")

def create(request):
    if request.method == "POST":
        form = MailForm(request.POST)
        if form.is_valid():
            print("ahora lidiamos con esto")
    else:
        form = MailForm()
    
    return render(request, "mails/create.html", {'form': form})

def get_templates(request):
    status_id = request.GET.get('status')
    if status_id:
        status = Status.objects.get(id=status_id)
    product_id = request.GET.get('product')
    if product_id:
        product = Product.objects.prefetch_related('partnergroup_set').get(id=product_id)
        partner_groups = product.partnergroup_set.all()

    if product and status:
        data = {
            'product': product.name,
            'subject': status.head,
            'content': status.body,
            'to': list(partner_groups.values()),
        }
    else:
        data = {}
    
    return JsonResponse(data)

    

