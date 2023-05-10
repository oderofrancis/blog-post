# blog-post

First git clone 

`git clone  https://github.com/oderofrancis/blog-post.git`

Navigate to the folder and create virtualenv

`cd blog-post`

`virtualenv env`

Activate virtualenv

For Windows 
`env/Scripts/activate`

for Linux

`. env/bin/activate`

Install the libraries from the requirements.txt file

`pip install -r requirements.txt`

Migrate the models to your database

`python manage.py migrate`

Create super user

`python manage.py createsuperuser`

Fill in your username, email and password

Then run server

`python manage.py runserver`

Navigate to admin and fill in your username and password.

http://127.0.0.1:8000/admin/

Add records in your admin blog post.

Then view them on you template in : http://127.0.0.1:8000/

### Have a nice coding time

