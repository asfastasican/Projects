from django import forms
from .models import *

class LeadForm(forms.ModelForm):
    class Meta:
        model= lead
        fields='__all__'