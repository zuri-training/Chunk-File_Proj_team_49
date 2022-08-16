from distutils import dir_util
import os
from django.conf import settings
from pathlib import Path
import boto3
from decouple import config



# def delete_zip_file(sender, instance, **kwargs):
#     # this reciever function is connected to a post_delete signal
#     # it deletes the zip file from the server when a chunk order
#     zip_location = instance.zip_link
#     dir_path = Path(__file__).resolve().parent.parent
#     print(dir_path)
#     location = str(dir_path) + zip_location
#     print("location of zip:" + location)
#     if os.path.exists(location):
#         os.remove(location)
#     else:
#         print("could not find file")
    

def delete_zip_file(sender,instance,**kwargs):
    s3file=instance.zip_link
    s3file=s3file.replace('https://chunk-it.s3.eu-west-3.amazonaws.com/','')
    try:
        s3 = boto3.client(
            "s3", aws_access_key_id=config('AWS_ACCESS_KEY_ID'), aws_secret_access_key=config('AWS_SECRET_ACCESS_KEY')
        )
        s3.delete_object(Bucket='chunk-it', Key=s3file)
        return True
    except Exception as ex:
        print(str(ex))
        return False