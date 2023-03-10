from django import forms
from django.contrib.auth.models import User
from phonenumber_field.formfields import PhoneNumberField
from django_countries.fields import CountryField
from .models import Cars, Models, Sell
from django.forms.widgets import DateInput
from django.contrib.auth.forms import UserChangeForm


class SellForm(forms.ModelForm):
    class Meta:
        model = Sell
        fields = '__all__'