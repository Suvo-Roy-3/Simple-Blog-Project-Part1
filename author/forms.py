from django import forms
from .models import Author
class authorForms(forms.ModelForm):
    class Meta:
        model=Author
        fields='__all__'
