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


class SignUpForm(UserCreationForm): 
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields['email'].widget.attrs.update({ 
            'name':'email', 
            'id':'email', 
            'type':'email',  
            })
        self.fields['fullname'].widget.attrs.update({ 
            'name':'fullname', 
            'id':'username', 
            'type':'text',  
            }) 
        self.fields['password1'].widget.attrs.update({ 
            'name':'password1', 
            'id':'password', 
            'type':'password',  
            }) 
        self.fields['password2'].widget.attrs.update({ 
            'name':'password2', 
            'id':'password2', 
            'type':'password',  
            })  
    class Meta: 
        model = CustomUser
        fields = ('email','fullname', 'password1', 'password2')

