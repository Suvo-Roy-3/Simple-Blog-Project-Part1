from django import forms
from .models import profiles
class profileForms(forms.ModelForm):
    class Meta:
        model=profiles
        fields='__all__'
