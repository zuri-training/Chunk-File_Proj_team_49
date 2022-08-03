from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignUpForm,PasswordChangeForm,PasswordResetForm,PasswordResetConfirm,LoginForm
from django.contrib.auth import  authenticate ,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views
from django.contrib.auth import login as auth_login


# Create your views here.
#register view with custom form
def register(request):
    if request.user.is_authenticated:
        return redirect('chunkapp:dashboard')
    if request.method == 'POST':
        form = SignUpForm(request.POST) 
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('chunkapp:dashboard')
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
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            user = authenticate(request,email=email, password=password)
            auth_login(request,user)
            return redirect('chunkapp:dashboard')
        else:
            form = LoginForm(request.POST)
            return render(request, 'accounts/login.html', {'form': form})
    else:
        form = LoginForm()
        return render(request, 'accounts/login.html', {'form': form})


def signout(request):
    logout(request)
    return redirect ('accounts:login')


class PasswordChange(auth_views.PasswordChangeView):
    template_name='accounts/password_change_form.html'
    form_class=PasswordChangeForm

class PasswordChangeDone(auth_views.PasswordChangeDoneView):
    template_name='accounts/password_change_done.html'

class PasswordReset(auth_views.PasswordResetView):
    template_name='accounts/password_reset_form.html'  
    form_class=PasswordResetForm
    #to be added
    email_template_name='accounts/password_reset_email.html' 
    #to be added
    subject_template_name="accounts/password_reset_subject.txt"

class PasswordResetDone(auth_views.PasswordResetDoneView):
    template_name='accounts/password_reset_done.html'

class PasswordResetConfirm(auth_views.PasswordResetConfirmView):
    template_name='accounts/password_reset_confirm.html'
    form_class=PasswordResetConfirm 

class PasswordResetComplete(auth_views.PasswordResetCompleteView):
    template_name='accounts/password_reset_complete.html'
    

