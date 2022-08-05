import json
import zipfile
import os
import pathlib
from pathlib import Path
import shutil
from zipfile import ZipFile, ZIP_DEFLATED
from django.conf import settings
import uuid
import pandas as pd
from .forms import FileUploadForm,ChunkSizeForm
BASE_DIR = settings.BASE_DIR
MEDIA_DIR = settings.MEDIA_ROOT
# the utils file is where all the business logic of file chunking file 
# validation and other technical operations and functions exist

#form wizard templates
TEMPLATES = {"fileupload": "chunkapp/dashboard.html",
             "chunksize": "chunkapp/chunksize.html",}
#form wizard forms
FORMS = [("fileupload", FileUploadForm),
         ("chunksize", ChunkSizeForm),]


def validateFile(UploadedFile):
    # this serves as validation for the Upload file form in django
    if UploadedFile.name.endswith('.csv') or UploadedFile.name.endswith(".json"):
        return UploadedFile

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
    return directory 


def zipFunction(directory):
          # # the first parameter in zipfile.Zipfile is the location where the zip file is saved
          #zip location
          zip_file_name = generateRandomName() + ".zip"
          zip_location=MEDIA_DIR + "/" + zip_file_name 
          with zipfile.ZipFile(zip_location, "w", ZIP_DEFLATED, compresslevel=2) as archive:
            for file_path in directory.iterdir():
              archive.write(file_path, arcname=file_path.name)
            archive.close()
          shutil.rmtree(directory)
        #   # this code is responsible for deleting the initial uploaded file
        #   dir_path = Path(__file__).resolve().parent / "media"
        #   file_path = dir_path / f.name
        #   file_path.unlink() # remove file
          return "/media/" + zip_file_name

def generateRandomName(file_name = ""):
    return str(uuid.uuid4()) + file_name

                              


def chunkCsv(csv_file, no_of_rows):
    line_number = sum(1 for row in (open(csv_file)))
    file_name = csv_file.name.strip(".")[0]
    file_location = generateRandomName(file_name)
    os.makedirs(MEDIA_DIR + "/" + file_location)
    for i in range(0, line_number, no_of_rows):
        df = pd.read_csv(csv_file, header=None, nrows=no_of_rows, skiprows=i)
        newfile = MEDIA_DIR + "/" + file_location +'/'+ str(i) + '.csv'
        df.to_csv(newfile,
                  index=False,
                  header=True,
                  mode='a',
                  chunksize=no_of_rows)
    dir=pathlib.Path(MEDIA_DIR + "/" + file_location + "/")                  
    return dir










# def split_csv(csvfilepath, rows_per_chunk):
#     file_line_number = len(pd.read_csv(csvfilepath))                           
#     batch_no = 1                                               
#     # if the number of rows specified per chunk by the user is greater than total number of lines in the file
#     if (rows_per_chunk > file_line_number):
#         print('Number of rows in a chunk cannot be greater than total number of lines in the file')

#     elif (rows_per_chunk < 1):      
#         print('Number of rows in a chunk cannot be less than 1')
#     else:
#         for chunk in pd.read_csv(csvfilepath, chunksize= rows_per_chunk ):
#             chunk.to_csv('chunk' + str(batch_no) + '.csv',  index=False)
#             batch_no += 1

# rows_per_chunk: is the number of rows the user wants per chunk file
# file_line_number: Total number of lines in the file 
# batch_no: number we will use to increment the file name of each chunk 
# csvfilepath: csv file path




# def handleUploadedFile(f):
#     # this function allows us to read a large file
#     # and download the file unto the server in an efficient manner
#     with open('media/' + f.name, 'wb+') as destination:
#         for chunk in f.chunks():
#             destination.write(chunk)
#     return destination