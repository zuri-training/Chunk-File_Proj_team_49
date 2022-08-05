from distutils import dir_util
import os
from django.conf import settings
from pathlib import Path



def delete_zip_file(sender, instance, **kwargs):
    # this reciever function is connected to a post_delete signal
    # it deletes the zip file from the server when a chunk order
    zip_location = instance.zip_link
    dir_path = Path(__file__).resolve().parent.parent
    print(dir_path)
    location = str(dir_path) + zip_location
    print("location of zip:" + location)
    if os.path.exists(location):
        os.remove(location)
    else:
        print("could not find file")
    