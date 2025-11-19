from django import forms

class PartnerGroupForm(forms.Form):
    name = forms.CharField(label="Nombre del grupo", max_length=100)