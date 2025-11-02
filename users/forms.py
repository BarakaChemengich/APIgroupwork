from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone = forms.CharField(max_length=15, required=False)
    is_traveler = forms.BooleanField(required=False)
    is_admin = forms.BooleanField(required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'phone', 'is_traveler', 'is_admin', 'password1', 'password2']
