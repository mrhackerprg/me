from django import forms
from .models import Contactme

class HomeForm(forms.Form):
    name = forms.CharField(max_length=30)
    email = forms.EmailField()
    number = forms.CharField()
    messages = forms.Textarea()