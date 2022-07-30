import json
import zipfile
import os
import pathlib
from pathlib import Path
import shutil
from zipfile import ZipFile, ZIP_DEFLATED
from django.forms import ValidationError
from django.conf import settings
import uuid
BASE_DIR = settings.BASE_DIR
MEDIA_DIR = settings.MEDIA_ROOT
# the utils file is where all the business logic of file chunking file 
# validation and other technical operations and functions exist

def validateFile(UploadedFile):
    # this serves as validation for the Upload file form in django
    if UploadedFile.name.endswith('.csv') or UploadedFile.name.endswith(".json"):
        return UploadedFile

def handleUploadedFile(f):
    # this function allows us to read a large file
    # and download the file unto the server in an efficient manner
    with open('media/' + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    return destination


def chunkJson(file_path, obj_count):
  #opens uploaded file
  with open(file_path,'r') as file:
    #validates it
    try:
        #stores the object in a list
        json_obj_list = json.load(file)
    except:
       print("Not working could not load json file")
    #set prefixes for each individual file  
    index=0
    #gets the media folder
    #i've made the base dir global
    #creates a new dir to store the chunks, the directory is randomly generated using UUID
    file_name = file.name.strip(".")[0]
    file_location = generateRandomName(file_name)
    os.makedirs(MEDIA_DIR + "/" + file_location)
    #to be renamed so that two folders never have the same name
    #loops through the objs in the list
    for json_obj in range(0,len(json_obj_list), obj_count):
        index=index+1
        directory_name= MEDIA_DIR + "/" + file_location + "/" +str(index)+'.json'

        with open(directory_name, 'w') as out_json_file:
            # Save each obj to their respective filepath
            # with pretty formatting thanks to `indent=4`    
            chunk=json_obj_list[json_obj:json_obj + obj_count]
            json.dump(chunk, out_json_file, indent=4)

    directory=pathlib.Path(MEDIA_DIR + "/" + file_location + "/")    
    return directory, file  


def zipFunction(directory,f):
          # # the first parameter in zipfile.Zipfile is the location where the zip file is saved
          #zip location
          zip_file_name = generateRandomName() + ".zip"
          zip_location=MEDIA_DIR + "/" + zip_file_name 
          with zipfile.ZipFile(zip_location, "w", ZIP_DEFLATED, compresslevel=2) as archive:
            for file_path in directory.iterdir():
              archive.write(file_path, arcname=file_path.name)
            archive.close()
          shutil.rmtree(directory)
          # this code is responsible for deleting the initial uploaded file
          dir_path = Path(__file__).resolve().parent / "media"
          file_path = dir_path / f.name
          file_path.unlink() # remove file
          return "/media/" + zip_file_name

def generateRandomName(file_name = ""):
    return str(uuid.uuid4()) + file_name