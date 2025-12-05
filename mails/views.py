from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from products.models import Product
from statuses.models import Status
from partner_groups.models import PartnerGroup
from partners.models import Partner
from .forms import MailForm
from utils.send_email import send_mjml_email
from .models import Mail, DeliveryStatus
import json

def show(request):
    return HttpResponse("Hola mails")

def create(request):
    if request.method == "POST":
        form = MailForm(request.POST)
        if form.is_valid():
            mail = Mail.objects.create(
                product = form.cleaned_data['product'],
                status = form.cleaned_data['status'],
                recipients = form.cleaned_data['recipients'],
                subject = form.cleaned_data['subject'],
                content = form.cleaned_data['content'],
            )
            recipients = json.loads(request.POST.get("recipients"))
            for recipient in recipients:
                partners = Partner.objects.filter(partner_group=recipient["value"])
                for partner in partners:
                    #send_mjml_email fue una función creada en la capeta de utils
                    result = send_mjml_email( 
                        to=partner.email,
                        subject=request.POST.get("subject"),
                        template="mails/send_notification.mjml",
                        context={
                            "content": request.POST.get("content")
                        }
                    )

                    DeliveryStatus.objects.create(
                        mail = mail,
                        partner_email = result["to"],
                        status = "OK" if result["ok"] else "FAILED",
                        code = result["error"]["code"] if result.get("error") is not None else "",
                        message = result["error"]["message"] if result.get("error") is not None else "",              
                    )
    else:
        form = MailForm()
    
    return render(request, "mails/create.html", {'form': form})

def get_templates(request): #Esta función se utiliza en el js autocomplete_notification para traer el texto de las notificaciones a los input una vez se seleccione producto y status
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

    

