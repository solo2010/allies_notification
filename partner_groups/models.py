from django.db import models

class PartnerGroup(models.Model):
    name = models.CharField(max_length=255) 
