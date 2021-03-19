from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *

class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields=['username','email','password1','password2']

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'


class DoctorForm(forms.ModelForm):
    class Meta:
        model=Doctor
        fields='__all__'

class MedicalForm(forms.ModelForm):
    class Meta:
        model=Medical
        fields='__all__'

class OrganizationForm(forms.ModelForm):
    class Meta:
        model=Organization
        fields='__all__'

class StocksAddForm(forms.ModelForm):
    class Meta:
        model:Stocks
        fields='__all__'
