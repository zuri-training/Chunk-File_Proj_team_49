<<<<<<< HEAD
=======
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignUpForm,PasswordChangeForm,PasswordResetForm,PasswordResetConfirm,LoginForm
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views


# Create your views here.
#register view with custom form
def register(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = SignUpForm(request.POST) 
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
    form = SignUpForm() 
    context = { 
                'form': form 
            } 
    return render(request, 'accounts/register.html', context)



#class based views extending django defaults and customising
class LoginView(auth_views.LoginView):
    template_name='accounts/login.html'
    authentication_form=LoginForm


class PasswordChange(auth_views.PasswordChangeView):
    template_name='accounts/password_change_form.html'
    form_class=PasswordChangeForm

class PasswordReset(auth_views.PasswordResetView):
    template_name='accounts/password_reset_form.html'  
    form_class=PasswordResetForm
    #to be added
    email_template_name='accounts/password_reset_email.html' 
    #to be added
    subject_template_name="accounts/password_reset_subject.txt"

class PasswordResetConfirm(auth_views.PasswordResetConfirmView):
    template_name='accounts/password_reset_confirm.html'
    form_class=PasswordResetConfirm    
    


>>>>>>> origin/main
