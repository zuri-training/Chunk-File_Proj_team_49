import re
from django.shortcuts import HttpResponse, render, redirect,HttpResponseRedirect
from . utils import BASE_DIR, handleUploadedFile, chunkJson ,zipFunction,chunkCsv
from . forms import FileUploadForm,ChunkSizeForm
from . models import ChunkOrder
from formtools.wizard.views import SessionWizardView
from django.core.files.storage import FileSystemStorage
import os
from django.conf import settings
from pathlib import Path
import pathlib
MEDIA_DIR = settings.MEDIA_ROOT
# the convention for creating a view is the view function 
# and view appended to the name, this is for simplicity and easy
# understanding of code 
# the view functions use a camelCase convention

#landing page view
def index(request):
    return render(request,'chunkapp/index.html')
#frequently asked questions view
def faq(request):
    return render(request,'chunkapp/faq.html')
#dashboard view
# def dashBoard(request):
#     # this views primary function is too render a template
#     # and then pass a form as the context
#     # form= FileUploadForm()
#     # context = {"form": form}
#     return render(request,'chunkapp/dashboard.html')

#dashboard upload wizard
class UploadWizard(SessionWizardView):
    template_name='chunkapp/dashboard.html'
    form_list = [FileUploadForm, ChunkSizeForm]
    file_storage = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'largefile'))
    def done(self,form_list,form_dict, **kwargs):
         form_data=process_form(form_list)
         return render(self.request, 'chunkapp/done.html', {'form_data':form_data})

def process_form(form_list):
    form_data =[form.cleaned_data for form in form_list]
    file=form_data[0]['file'].name
    chunk_size=form_data[1]['chunk_size']
    path =pathlib.Path(MEDIA_DIR + "/largefile/" + file)
    if file.endswith('.json'):
        dir=chunkJson(path, chunk_size)
    elif file.endswith('.csv'):
        dir= chunkCsv(path,chunk_size)    
    return zipFunction(dir)



# def uploadFile(request):
#     if request.method == 'POST':
#         form = FileUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             # file is saved
#             file=form.save()
#             return render(request, 'chunkapp/new.html', {'form': ChunkSizeForm}) 
#     else:
#         form = FileUploadForm()
#     return render(request, 'chunkapp/dashboard.html', {'form': form,'file':file})

# def setChunkSize(request):
#         form = ChunkSizeForm(request.POST)
#         if form.is_valid():
#             # file is saved
#             file= form.save()
#             return HttpResponse('saved')
#         return render(request, 'chunkapp/new.html', {'form': form})   

#chunk file view
# def chunkFileView(request):
#     # this views primary function is to chunk the uploaded files
#     # it is also responsible for validating the chunk_order_form
#     if request.method == "POST":
#         chunk_order_form = ChunkOrderForm(request.POST, request.FILES)
#         if chunk_order_form.is_valid():
#             # if the form that takes in the chunk order request is valid 
#             # now we can start the chunking process

#             # first we get the type of file that was uploaded
#             # and then download it unto the server
#             file = handleUploadedFile(request.FILES['file'])
#             file_name = file.name
#             file_type = file_name.split(".")[1]
#             chunk_size = chunk_order_form.cleaned_data['chunk_size']
#             file_location = BASE_DIR / file_name
#             chunk_location, file = chunkJson(file_location, chunk_size)
#             zip_link = zipFunction(chunk_location, file)
#             # after the file type is gotten we pass to a function that chunks the file
#             order = ChunkOrder.objects.create(file_name = file_name, chunk_size = chunk_size, zip_link = zip_link)
#             return HttpResponse(file_type)
#         else:
#             # this else case shows that chunk order request was invalid
#             # it then redirects the user back to the dashboard
#             redirect("dashboard")
#list recent chunks view
def listRecentChunks(request):
    recent_chunks=ChunkOrder.objects.all()
    context={
        'recent_chunks':recent_chunks
    }          
    return render(request,'chunkapp/recent.html',context)
#terms an conditions view
def termsAndConditions(request):
    return render(request ,'chunkapp/toc.html')    
#how to use view
def howTouse(request):
    return(request,'chunkapp/howtouse.html')

