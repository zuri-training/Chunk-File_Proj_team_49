# chunk_it
chunk large json &amp; csv files

# chunk_it
## Run locally.

If you want to run locally,then you can use the following command to run locally on your machine:


Clone the project
```
  git clone git@github.com:zuri-training/Chunk-File_Proj_team_49.git
```

Go to the project directory
```
  cd Chunk-File_Proj_team_49.git
```

Create a Virtual Environment 
```
python -m venv venv
```

Activate Virtual Environment
```
venv\scripts\activate
```

Install Dependencies
```
  pip install -r requirements.txt
```

make migrations
```
python manage.py makemigrations
```

Migrate the database
```
python manage.py migrate
```

create superuser 
```
python manage.py createsuperuser
```

Create a new branch to work with
```
git branch <new-branch>
```

switch to the new branch to make changes
```
git checkout <new-branch>
```

Finally, Start The Server.
```
python manage.py runserver
```
*important*
Always pull before making new changes
After making changes Do not merge,push the branch you made changes on to the repo,and then make a pull request on github




