from django import forms
from products.models import Product

class PartnerGroupForm(forms.Form):
    name = forms.CharField(label="Nombre del grupo", max_length=100)
    # product = forms.ModelChoiceField(label="Producto",
    #     queryset=Product.objects.all(),
    #     empty_label="Selecciona el producto que consume"
    # )