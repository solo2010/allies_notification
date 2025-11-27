from django.db import models
from products.models import Product
from statuses.models import Status

class Mail(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL, null=True, related_name='mails')
    status = models.ForeignKey(Status, on_delete=models.SET_NULL, null=True, related_name='mails')
    recipients = models.JSONField(default=list, help_text="Lista de Correos con estado de envio")
    subject = models.CharField(max_length=500)
    contet = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True, null=True)
    update_date = models.DateTimeField(auto_now=True, null=True)
