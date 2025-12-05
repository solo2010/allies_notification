from django.db import models
from products.models import Product
from statuses.models import Status

class Mail(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL, null=True, related_name='mails')
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, related_name='mails')
    recipients = models.JSONField(default=list, help_text="Lista de Correos con estado de envio")
    subject = models.CharField(max_length=500)
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        db_table = "mails"

class DeliveryStatus(models.Model):
    mail = models.ForeignKey(Mail, on_delete=models.SET_NULL, null=True, related_name='deliveries_status')
    partner_email = models.EmailField(null=True)
    status = models.CharField(max_length=300)
    code = models.CharField(max_length=300)
    message = models.CharField(max_length=5000)

    class Meta:
        db_table = "deliveries_status"