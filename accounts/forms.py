from django.contrib.auth.forms import UserChangeForm, UserCreationForm, UserCreationForm,AuthenticationForm,PasswordChangeForm,PasswordResetForm,SetPasswordForm
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

#sign up custom form
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

        
#login custom form
class LoginForm(AuthenticationForm):
    #customizing auth form
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        self.fields.pop('username')
        self.fields['email'].widget.attrs.update({ 
             'name':'email',
             'id':'email',
             'type':'text',
             'placeholder': '  ', 
             'class': 'form__input',
            
             }) 
        self.fields['password'].widget.attrs.update({ 
            'name':'password', 
            'id':'password', 
            'type':'password',
            'class': 'form__input', 
            'placeholder': ' ', 
            }) 
    email = forms.EmailField(max_length=100)
    class Meta: 
        model = CustomUser
        fields = ('email', 'password')    


#password change custom form
class PasswordChangeForm(PasswordChangeForm):
     def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields['old_password'].widget.attrs.update({ 
            'name':'password', 
            'id':'current-password', 
            'type':'password',  
            })
        self.fields['new_password1'].widget.attrs.update({ 
            'name':'password1', 
            'id':'password', 
            'type':'password',  
            }) 
        self.fields['new_password2'].widget.attrs.update({ 
            'name':'password2', 
            'id':'password2', 
            'type':'password',
            }) 


#password reset form custom form
class PasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields['email'].widget.attrs.update({ 
            'name':'email', 
            'id':'email', 
            'type':'email',  
            })


#password reset confirm custom form , the email being sent
class setPasswordForm(SetPasswordForm):
     def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields['new_password1'].widget.attrs.update({ 
            'name':'password', 
            'id':'password', 
            'type':'password',  
            })
        self.fields['new_password2'].widget.attrs.update({ 
            'name':'password', 
            'id':'password', 
            'type':'password2',  
            })