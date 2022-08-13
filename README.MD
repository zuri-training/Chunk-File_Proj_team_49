# chunk49 
A platform for splitting large json and csv files
## Appendix
>- Logo
>- Chunk49 
>- About Us
>- Features
>- Run Locally
>- Documentation
>- Acknowledgements
>- Tech Stack
>- Usage/Examples
>- Screenshots
>- Used By
>- Links
>- Frequently Asked Questions (FAQ)
>- Support
>- Badges
>- Contribution
>- Authors

## Logo
![Logo](https://i.im.ge/2022/08/09/FKfg0C.Group25.png)
​

## Chunk49
>Chunk49 is a platform that accepts large json and csv files and splits them into smaller bits.
​ The product provides users with high quality output files with less the size of the original file in a zipped format. Our well-designed platform also affords users irrespective of technological knowledge an easy to navigate structure with an aesthetically appealing view.

## About Us
>We're a fast growing team of designers and developers who's aim is providing top-notch service that's second to none.
You can find out more about us on our website's "About us" page.
​
## Features

>- Free access to product for signed-up users
>- Acces to product information for visiting users
>- Chunking of Json files
>- Chunking of CSV files
>- Accepts large files
>- Accepts upload from file manager
>- Displays selected file name
>- Allows users select number of lines in split files
>- Download split files
>- Save split files to download later.
>- Mobile compatible
>- Laptop/Desktop compatible
>- Output in zipped format
>- Reduces output size of chunked files
>- Chunking history available
>- Support available
>- Forgot password
>- Frequently asked questions available in the FAQ section.
​
## Run locally
​
If you want to run locally, then you can use the following commands on your machine:
​
​

Clone the project
```
  git clone https://github.com/zuri-training/Chunk-File_Proj_team_49.git
```
​
Go to the project directory
```
  cd Chunk-File_Proj_team_49.git
```
​
Create a Virtual Environment 
```
python -m venv venv
```
​
Activate Virtual Environment
```
venv\scripts\activate
```
​
Install Dependencies
```
  pip install -r requirements.txt
```
​
make migrations
```
python manage.py makemigrations
```
​
Migrate the database
```
python manage.py migrate
```
​
create superuser 
```
python manage.py createsuperuser
```
​
Create a new branch to work with
```
git branch <new-branch>
```
​
switch to the new branch to make changes
```
git checkout <new-branch>
```
​
Finally, Start The Server.
```
python manage.py runserver
```
## AIDED DEPLOYMENT FOR CHUNK 49
understanding our folder structure chunk49
1. We have two custom built django applications
	Accounts application for auth
	chunkapp which contains our business logic and major routing
2. media\largefile - this is for local deployment our files,
3. templates - contains our html pages for each application
4. staticfiles contains all our static files
5. requirements.txt contains all our dependencies needed for this project to work.
 
After cloning the project and downloading the dependencies create a .env file
in the same directory as the settings.py -DIRECTORY: Chunk-File_Proj_team_49/chunk49/
and then copy and paste the env configuration inside this file. Click on the link below to view the env configuration.

USERNAME: mike 
PASSWORD: chunk49
```
https://tinyurl.com/2ove2tjn
```
there is a one time access to that link after the first login, the link becomes useless
if you face this issue, please contact 
@Syntexh
or
@Okputu Julius
or
@Evelyn Jacobs
on slack
this is a security measure.

## Documentation
>Access our documentations on:
>* [Documentation](https://docs.google.com/document/d/1-j1eAx3WyY-UOxUvCAcACpjoT5xDkgQYWECG1wvqivw/edit)
>* [DOCUMENTATION.MD](https://github.com/zuri-training/Chunk-File_Proj_team_49/blob/main/DOCUMENTATION.MD)
​
## Acknowledgements
>​- Zuri Team
​
​
​
## Tech Stack
>This site was built using the following tools:
>* HTML
>* CSS BOOTSTRAP
>* jAVASCRIPT
>* PYTHON(Django)
​
​
## Usage/Examples
​
**Landing page Navigation:**

>At the top-right bar of the landing page, you'll find the signup and login button which you can use to either signup or login from. Or you can make use of the "get started" button which automatically takes you to the sign-up page. Need information on the product? Then easily get it from this page.
​
 
**USING THE DASHBOARD:**

>On the dashboard you can:
>>●	Upload your files
> 
>>●	Select the size of the file
> 
>>●	View your chunking history
> 
>>●	Change settings selections
> 
>>●	Logout
> 
>❖	**Upload your files;** 
> 
> Click on the arrow icon and select your desired chunking file, this will automatically upload it for chunking. 
> 
>❖	**Select file size;**
>
>Select desired chunked file size. Do this using the top-down arrow selector. After successful selection, click start to begin the chunking process.
>
>❖  **View your chunking history;**
>
>At the left side of your dashboard, you'll find a link to your chunking history.
​
>
>❖	**Change settings selection;**
>
>At the bottom of the left side navigation is the settings. Make your desired changes from this section.
​
>
>❖	**Logout;**
>
>Done with chunking? Then use the logout button. 
​
>
>❖	**Login;**
>
>When returning to our platform to perform another chunking, use the login button to gain access into your dashboard
 
​
**CHUNKING A FILE:**

>Only upload your large CSV or Json files for chunking, other formats are currently not available.
>
>●   Download or 
​
>
>●   Save for later
​
>
>❖  Download button;
When selected will download your chunked file directly into your downloads folder
>
>●	Save for later;
Save your chunked file on or server for up to 24hours to before downloading
​
​
​
​
​
## Screenshots
​
[Website Screenshots](https://docs.google.com/document/d/1UtIpIDsbtg44I-vVW80Y-rLInIWVnnPzY2JPnSCOCP0/edit?usp=sharing)
​
​
## Used By

>This project is used by the following companies:
​
>- Zuri
​
## Links
>Product link:
>
>​
>[Github](https://github.com/zuri-training/Chunk-File_Proj_team_49)
​
>
>[HeroKuapp](https://chunk-it.herokuapp.com/)
## FAQ

#### What is chunking and why should i chunk my file

 >A chunked file is one reduced to smaller bits or chunks  thereby canceling repetition in the file.

​
#### What are the chunking options 

>We currently provide two options which are csv and json, with possibility of additing more options in future.

​
#### Is there a chunking limit 
>There is no limit to how much you can chunk.

​
#### Is there a fee for chunking my files
>chunk49 is a free web platform that doesn't require you to pay before chunking. However, you must register to gain access into the chunking dashboard. 

​
#### How long is the chunking process 
>This depends on a number of factors such as the file size and your network speed.

​
#### Do i need special skills to use Chunk49 
>Aside from uploading, all processess involved in chunking your files are carried out from our system and no action is required from your end.

​
#### I tried chunking a file on your platform  but it didnt work, why?
>We currently accept files in csv and json formats, any other format apart from these specified will be rejected. 
​
​

## Support

>For support, you can reach us on chunk49@yahoo.com or send us a message on Chunk49 "Contact us" page.
​
​
## Badges

​

[![Github Stars](https://img.shields.io/github/stars/zuri-training/Chunk-File_Proj_team_49)]

[![Github Forks](https://img.shields.io/github/forks/zuri-training/Chunk-File_Proj_team_49?color=green)]


## Contribution

>If you have a contribution that will help improve chunk49, simply contact us with your contribution(s) on our contact us page. All contributions you make are greatly appreciated.
​
## Authors

>- [@Eruanga](https://www.github.com/Eruanga)
>- [@Eva-Jacobs](https://www.github.com/Eva-jacobs)
