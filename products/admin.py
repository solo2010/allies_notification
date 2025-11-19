from django.contrib import admin
from .models import Product

class productAdmin(admin.ModelAdmin):
    list_display = ["name"]

admin.site.register(Product, productAdmin)


