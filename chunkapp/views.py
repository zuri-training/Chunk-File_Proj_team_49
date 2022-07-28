from django.shortcuts import render

# Create your views here.
def dashboard(request):
    return render(request, 'chunkapp/dashboard.html', { })

def index(request):
    return render(request, 'chunkapp/index.html')
