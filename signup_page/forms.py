from django.forms import ModelForm
from .models import Signup
from django import forms


class SignupForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = "__all__"
