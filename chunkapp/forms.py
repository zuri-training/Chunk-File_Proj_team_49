from . models import ChunkOrder
from django.forms import ModelForm


# this is the form that takes in the required entries to chunk a file
# the file to be chunked is also uploaded within this form along with
# the size of chunks
# class ChunkOrderForm(forms.Form):
#     # the file field is for the file that is to be uploaded
#     # the chunk size is to determine how the file is going to be chunked
#     file = forms.FileField(validators=[validateFile])
#     chunk_size = forms.IntegerField()

class FileUploadForm(ModelForm):
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields['file'].widget.attrs.update({ 
            'name':'email', 
            'id':'email', 
            'type':'email',  
            })
    class Meta:
        model=ChunkOrder
        fields=['file']

class ChunkSizeForm(ModelForm):
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs) 
        self.fields['chunk_size'].widget.attrs.update({ 
            'name':'email', 
            'id':'email', 
            'type':'email',  
            })
    class Meta:
        model=ChunkOrder
        fields=['chunk_size']

