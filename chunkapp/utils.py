import pandas as pd
import os

#filepath is the path of the csv file
#rows_per_chunk is the number of rows the user wants in each csv chunk 
#batch_no is the we will use to increment the file name of each chunk
#file_line_number is the number of lines in the uploaded csv file

filepath = 'myFile2.csv'        
rows_per_chunk =  5000                                    

# ============ End Input =================

def split_csv(filepath, rows_per_chunk):
    file_line_number = len(pd.read_csv(filepath))                              
    batch_no = 1                                                

    if (rows_per_chunk > file_line_number):
        print('Number of rows in a chunk cannot be greater than total number of lines in the file')
    elif (rows_per_chunk < 1):      
        print('Number of rows in a chunk cannot be less than 1')
    else:
        for chunk in pd.read_csv(filepath, chunksize= rows_per_chunk ):
            chunk.to_csv('chunk' + str(batch_no) + '.csv',  index=False)
            batch_no += 1

split_csv(filepath, rows_per_chunk)