from django.db import models
from products.models import Product

class PartnerGroup(models.Model):
    name = models.CharField(max_length=255)
    products = models.ManyToManyField(Product, through='partner_groups.PartnerGroupProduct')

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = "partner_groups"
    
class PartnerGroupProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    partnergroup = models.ForeignKey(PartnerGroup, on_delete=models.CASCADE)

    def __str__(self):
        return f"{ self.product } - {self.partnergroup}"
    
    class Meta:
        db_table = "partnergroups_products"
