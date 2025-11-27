from django.db import models
from partner_groups.models import PartnerGroup

class Partner(models.Model):
    partner_group = models.ForeignKey(PartnerGroup, on_delete=models.CASCADE, related_name="partners")
    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    cellphone = models.CharField(max_length=25)




