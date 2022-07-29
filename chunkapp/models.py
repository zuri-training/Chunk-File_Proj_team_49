from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.

class ChunkOrder(models.Model):
    # this custom_user is linked directly to the custom_User class created in the accounts app
    # the file_name field refers to the name of the file that is chuncked during this chunkOrder

    # the chunk_size field is how many objects in  JSON or rows in CSV file to chunk by
    # this size should be based on the type of file that is being uploaded

    # the created field will log the time that a successful order for chunking occured
    # this field is important as it allows for quering the database 
    custom_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True)
    file_name = models.CharField(max_length=200, null=True, blank=True)
    zip_file = models.FileField(null=True, blank=True)
    chunk_size = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)

    # these properties like the file name saves a reference to the inital file type that was uploaded

    @property
    def file_type(self):
        return self.file_name.split(".")[1]
    
    def __str__(self) -> str:
        return super().__str__()
