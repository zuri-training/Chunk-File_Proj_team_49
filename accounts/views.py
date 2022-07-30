from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User


from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
# def register(request):
#     return render(request, 'register.html')
def password_change_done(request):
    return render(request, 'password_change_done.html')

def register(request):
    if request.method == 'POST':
        firstname = request.POST['fullname'].split(' ')[0]
        lastname = request.POST['fullname'].split(' ')[1]
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
            else:
                user = User.objects.create_user(firstname = firstname, lastname = lastname, password = password1, email = email)
                user.save()
                print('user created successfully')
        else:
            print('password not matching..')
    else:
        return render(request, 'accounts/register.html')
    return redirect('/')
