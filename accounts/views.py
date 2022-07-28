from django.shortcuts import render

# Create your views here.
def register(request):
    return render(request, 'register.html')
def password_change_done(request):
    return render(request, 'password_change_done.html')