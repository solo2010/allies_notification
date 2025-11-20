from django import forms

class StatusForm(forms.Form):
    status = forms.CharField(label="Status", max_length=100)