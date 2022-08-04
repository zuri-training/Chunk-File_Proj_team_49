from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignUpForm,PasswordChangeForm,PasswordResetForm,SetPasswordForm,LoginForm, setPasswordForm
from django.contrib.auth import  authenticate ,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from django.contrib.auth import login as auth_login
from django.urls import reverse_lazy
from django.contrib.auth import logout as auth_logout


# Create your views here.
#register view with custom form
def register(request):
    if request.user.is_authenticated:
        return redirect('chunkapp:dashboard')
    if request.method == 'POST':
        form = SignUpForm(request.POST) 
        if form.is_valid():
            print('valid form')
            user = form.save()
            auth_login(request, user)
            return redirect('chunkapp:dashboard') 
        else:
            form = SignUpForm() 
            messages.error(request, 'user with this email already exist.') 
            return render(request, 'accounts/register.html', {'form': form})   

    form = SignUpForm() 
    context = { 
                'form': form 
            } 
    return render(request, 'accounts/register.html', context)


def login(request):
    if request.user.is_authenticated:
        return redirect('chunkapp:dashboard')
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email').lower()
            password = form.cleaned_data.get('password')
            user = authenticate(request,email=email, password=password)
            if user is not None:
                auth_login(request,user)
                return redirect('chunkapp:dashboard')
            else:
                form = LoginForm(request.POST)
                messages.error(request, 'user with this email does not exist.') 
                return render(request, 'accounts/login.html', {'form': form})         
        else:
            form = LoginForm(request.POST)
            return render(request, 'accounts/login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})


def logout(request):
    auth_logout(request)
    return redirect ('accounts:login')

class PasswordChange(auth_views.PasswordChangeView):
    success_url=reverse_lazy('accounts:password_change_done')
    template_name='accounts/password_change_form.html'
    form_class=PasswordChangeForm
    

class PasswordChangeDone(auth_views.PasswordChangeDoneView):
    template_name='accounts/password_change_done.html'

class PasswordReset(auth_views.PasswordResetView):
    template_name='accounts/password_reset_form.html'  
    form_class=PasswordResetForm
    email_template_name='accounts/password_reset_email.html' 
    subject_template_name="accounts/password_reset_subject.txt"
    success_url=reverse_lazy('accounts:password_reset_done')

class PasswordResetDone(auth_views.PasswordResetDoneView):
    template_name='accounts/password_reset_done.html'

class PasswordResetConfirm(auth_views.PasswordResetConfirmView):
    template_name='accounts/password_reset_confirm.html'
    form_class=setPasswordForm
    success_url=reverse_lazy('accounts:password_reset_complete')

class PasswordResetComplete(auth_views.PasswordResetCompleteView):
    template_name='accounts/password_reset_complete.html'
    

