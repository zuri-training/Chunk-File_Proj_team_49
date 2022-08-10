import email
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
from .models import CustomUser


# Create your views here.
#register view with custom form
def register(request):
    if request.user.is_authenticated:
        return redirect('chunkapp:dashboard')
    if request.method == 'POST':
        form = SignUpForm(request.POST) 
        if form.is_valid():
            email = form.cleaned_data['email']
            if CustomUser.objects.get(email=email) is not None:
                messages.info(
                    request, 'User already exists! Try logging in.')
                return render(request, 'accounts/register.html', {'form': form})
            else:
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

#login view
def login(request):
    if request.user.is_authenticated:
        return redirect('chunkapp:dashboard')
    if request.method == "POST":
        form = LoginForm(data=request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email').lower()
            password = form.cleaned_data.get('password')
            try:
               user = CustomUser.objects.get(email=email)
            except:
               form = LoginForm()
               messages.error(request, 'User does not exist')
               return render(request, 'accounts/login.html', {'form': form})

            user = authenticate(request,email=email, password=password)

            if user is not None:
                auth_login(request,user)
                return redirect('chunkapp:dashboard')
            else:
                form = LoginForm(request.POST)
                messages.error(request, ' password is incorrect.') 
                return render(request, 'accounts/login.html', {'form': form})         
        else:
            form = LoginForm()
            messages.error(request, ' email is invalid.')
            return render(request, 'accounts/login.html', {'form': form})
        
    form = LoginForm()
    return render(request, 'accounts/login.html', {'form': form})

#logout view
def logout(request):
    auth_logout(request)
    return redirect ('accounts:login')

#password change view
class PasswordChange(auth_views.PasswordChangeView):
    success_url=reverse_lazy('accounts:password_change_done')
    template_name='accounts/password_change_form.html'
    form_class=PasswordChangeForm
    
#password change done view
class PasswordChangeDone(auth_views.PasswordChangeDoneView):
    template_name='accounts/password_change_done.html'

#password reset view
class PasswordReset(auth_views.PasswordResetView):
    template_name='accounts/password_reset_form.html'  
    form_class=PasswordResetForm
    email_template_name='accounts/password_reset_email.html' 
    subject_template_name="accounts/password_reset_subject.txt"
    success_url=reverse_lazy('accounts:password_reset_done')

#password reset done view
class PasswordResetDone(auth_views.PasswordResetDoneView):
    template_name='accounts/password_reset_done.html'

#password reset confirm view with custom forms
class PasswordResetConfirm(auth_views.PasswordResetConfirmView):
    template_name='accounts/password_reset_confirm.html'
    form_class=setPasswordForm
    success_url=reverse_lazy('accounts:password_reset_complete')

#password reset complete view
class PasswordResetComplete(auth_views.PasswordResetCompleteView):
    template_name='accounts/password_reset_complete.html'
    

