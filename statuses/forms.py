from django import forms

class StatusForm(forms.Form):
    status = forms.CharField(label="Status", max_length=100)
    head = forms.CharField(label="Cabezera", max_length=300)
    body = forms.CharField(
        label="Cuerpo",
        widget=forms.Textarea(attrs={'row': 4, 'cols': 40})
    )