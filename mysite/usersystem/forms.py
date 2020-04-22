from django import forms
from django.forms import ModelForm
from .models import Clients
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit


class UserForm(forms.ModelForm):

    class Meta():
        model = Clients
        fields = {'firstname', 'lastname', 'cnic', 'dob', 'age', 'gender', 'password'}







