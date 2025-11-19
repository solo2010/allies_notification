from django import forms

class ProductForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=100)