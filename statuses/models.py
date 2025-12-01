from django.db import models

class Status(models.Model):
    status = models.CharField(max_length=255)
    head = models.CharField(max_length=500, default="Sin cabezera")
    body = models.TextField(default="Sin cuerpo")

    def __str__(self):
        return self.status