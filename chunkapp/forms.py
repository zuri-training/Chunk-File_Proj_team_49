from django import forms


# this is the form that takes in the required entries to chunk a file
# the file to be chunked is also uploaded within this form along with
# the size of chunks
class ChunkOrderForm(forms.Form):
    # the file field is for the file that is to be uploaded
    # the chunk size is to determine how the file is going to be chunked
    file = forms.FileField(error_messages="Uploaded the wrong file type")
    chunk_size = forms.IntegerField()
