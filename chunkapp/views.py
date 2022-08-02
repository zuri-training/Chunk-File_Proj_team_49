from django.shortcuts import HttpResponse, render, redirect
from . utils import BASE_DIR, handleUploadedFile, chunkJson ,zipFunction
from . forms import ChunkOrderForm
from . models import ChunkOrder
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
def renderDashBoardView(request):
    # this views primary function is too render a template
    # and then pass a form as the context
    chunk_order_form = ChunkOrderForm()
    context = {"form": chunk_order_form}
    return render(request, 'chunkapp/dashboard.html', context)
#chunk file view
def chunkFileView(request):
    # this views primary function is to chunk the uploaded files
    # it is also responsible for validating the chunk_order_form
    if request.method == "POST":
        chunk_order_form = ChunkOrderForm(request.POST, request.FILES)
        if chunk_order_form.is_valid():
            # if the form that takes in the chunk order request is valid 
            # now we can start the chunking process

            # first we get the type of file that was uploaded
            # and then download it unto the server
            file = handleUploadedFile(request.FILES['file'])
            file_name = file.name
            file_type = file_name.split(".")[1]
            chunk_size = chunk_order_form.cleaned_data['chunk_size']
            file_location = BASE_DIR / file_name
            chunk_location, file = chunkJson(file_location, chunk_size)
            zip_link = zipFunction(chunk_location, file)
            # after the file type is gotten we pass to a function that chunks the file
            order = ChunkOrder.objects.create(file_name = file_name, chunk_size = chunk_size, zip_link = zip_link)
            return HttpResponse(file_type)
        else:
            # this else case shows that chunk order request was invalid
            # it then redirects the user back to the dashboard
            redirect("dashboard")
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

