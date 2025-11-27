from django import forms
from partner_groups.models import PartnerGroup
from .models import Partner

class PartnerForm(forms.Form):
    full_name = forms.CharField(label="Nombre Completo",max_length=100)
    email = forms.EmailField(label="Email")
    cellphone = forms.CharField(label="Número de Celular",max_length=100)
    partner_group = forms.ModelChoiceField(label="Grupo Aliado",
        queryset=PartnerGroup.objects.all(),
        empty_label="Seleccione el grupo aliado"
    )

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Partner.objects.filter(email=email).exists():
            raise forms.ValidationError("Esta email ya está registrado.")
        return email