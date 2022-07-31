from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import SignUpForm
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
# def register(request):
#     return render(request, 'register.html')
def password_change_done(request):
    return render(request, 'password_change_done.html')

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST) 
        if form.is_valid():
            form.save()  
            print('valid form')
    form = SignUpForm() 
    print('invalid form')
    context = { 
            'form': form 
        } 

    return render(request, 'accounts/register.html', context)