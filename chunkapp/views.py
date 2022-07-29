from django.shortcuts import render
from . forms import ChunkOrderForm
# the convention for creating a view is the view function 
# and view appended to the name, this is for simplicity and easy
# understanding of code 
# the view functions use a camelCase convention

def renderDashBoardView(request):
    # this views primary function is too render a template
    # and then pass a form as the context
    chunk_order_form = ChunkOrderForm()
    context = {"form": chunk_order_form}
    return render(request, 'chunkapp/dashboard.html', context)

def chunkFileView(request):
    # this views primary function is to chunk the uploaded files
    # it is also responsible for validating the chunk_order_form
    if request.method == "POST":
        chunk_order_form = ChunkOrderForm(request.POST, request.FILES)
        file = request.FILES