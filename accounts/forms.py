from django.contrib.auth.forms import UserChangeForm, UserCreationForm, UserCreationForm
from .models import CustomUser
from django import forms 
from django.contrib.auth.models import User 


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = '__all__'


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

