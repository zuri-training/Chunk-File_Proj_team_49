# these are all my tasks in the project phase

## Add custom user model,managers and tests
 [issue](https://github.com/zuri-training/Chunk-File_Proj_team_49/issues/20)
 i created a custom user model,added a custom manager for it and wrote unit tests for them
 links to files i worked on : [manager](https://github.com/zuri-training/Chunk-File_Proj_team_49/blob/main/accounts/managers.py),
 [models](https://github.com/zuri-training/Chunk-File_Proj_team_49/blob/main/accounts/models.py),[tests](https://github.com/zuri-training/Chunk-File_Proj_team_49/blob/main/accounts/tests.py)
 

## create alogrithm that chunks csv by no of rows
[issue](https://github.com/zuri-training/Chunk-File_Proj_team_49/issues/29)
i used python's pandas module to create an algorithm that chunks large csv files by a given number of rows 
the function takes in two parameters the file and the number of rows and chunks the file into smaller files by the specified number of rows
links to file i worked on: [utils](https://github.com/zuri-training/Chunk-File_Proj_team_49/blob/main/chunkapp/utils.py)

## create function that zip files
[issue](https://github.com/zuri-training/Chunk-File_Proj_team_49/issues/30)
i created a function that takes the dir from the function that chunks the file zips and compresses them
link to file i worked on [utils](https://github.com/zuri-training/Chunk-File_Proj_team_49/blob/main/chunkapp/utils.py)

## implement custom django forms/add template tags 
i created two model forms and customized them in the init function
and i rendered them in their correspomding templates
link to file i worked on[forms](https://github.com/zuri-training/Chunk-File_Proj_team_49/blob/main/chunkapp/forms.py)

## add ERD
i created a basic ERD diagram using drawsql

## add customized auth views
i extended the default django auth views(password_change,password_reset,logout) to have custom templates and redirects,i also customized their respective forms
link to files i worked on :[views](https://github.com/zuri-training/Chunk-File_Proj_team_49/blob/main/accounts/views.py),[forms](https://github.com/zuri-training/Chunk-File_Proj_team_49/blob/main/accounts/forms.py)

## create form wizard and form processor for the dashboard
i used the formtools django package to create a form that can span across two pages storing info in sessions,and a processor function that takes the data to process
link to file i worked on [views](https://github.com/zuri-training/Chunk-File_Proj_team_49/blob/main/chunkapp/views.py)


## connect dashboard templates to backend
i connected the dashboard templates to the backend functionality
link to file i worked on [chunkapp/](https://github.com/zuri-training/Chunk-File_Proj_team_49/tree/main/templates/chunkapp)

## Add views for listing recent chunks(zip)
i added a view that lists all the recent files
file i worked on [views](https://github.com/zuri-training/Chunk-File_Proj_team_49/blob/main/chunkapp/views.py)
