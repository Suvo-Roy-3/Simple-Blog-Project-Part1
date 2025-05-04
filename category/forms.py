from django import forms
from .models import category
class categoryForms(forms.ModelForm):
    class Meta:
        model=category
        fields='__all__'
