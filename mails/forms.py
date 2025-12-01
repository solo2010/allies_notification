from django import forms
from products.models import Product
from statuses.models import Status

class MailForm(forms.Form):
    product = forms.ModelChoiceField(label="Producto",
        queryset=Product.objects.all(),
        empty_label="Seleccione el producto con la novedad",
        widget=forms.Select(attrs={'id': 'product'}))
    status = forms.ModelChoiceField(label="Estado",
        queryset=Status.objects.all(),
        empty_label="Seleccione el estado del producto",
        widget=forms.Select(attrs={'id': 'status'}))
    recipients = forms.CharField(label="Grupo a notificar", 
        max_length=500, 
        widget=forms.TextInput(attrs={'id': 'recipients'}))
    subject = forms.CharField(label="Asunto", 
        max_length=500,
        widget=forms.TextInput(attrs={'id': 'subject'}))
    content = forms.CharField(
        label="Contenido",
        widget=forms.Textarea(attrs={'row': 4, 'cols': 40, 'id': 'content'})
    )


