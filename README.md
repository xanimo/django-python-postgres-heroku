# xanimo.herokuapp.com
xanimo.herokuapp.com, built with Django and Python.

## Understand
This is a simple application in Python that allows users to store snippets for future reference.

## Tests
In order to run this locally, clone this repo then:
Create a virtual environment 
```
virtualenv env
```

Activate the virtual environment  
```
source env/bin/activate
```

Then while in the virtual environment... 

Install the application requirements with either of the following commands
```
pip3 install -r requirements.txt
```

Run migrate
```
python3 manage.py migrate
```

Run the server at PORT 8000
```
python3 manage.py runserver
```

## Deployment
Everything you need for deployment to heroku works out of the box with the exception of seeding the postgres db and running createsuperuser.

After creating a new application on heroku, go through the usual steps towards deployment:
```
heroku git:remote -a yournewapp
git add .
git commit -am 'make it better'
git push heroku master
```
Once the application is deployed, go to the heroku site and open the console in your yournewapp's section and run the following commands:
```
python3 manage.py makemigrations
python3 manage.py migrate
```
These will 1) create new migration based on changes detected to your models and 2) synchronize the database state with the current set of models and migrations.

Finally run and complete the steps needed to create a super user:
```
python3 manage.py createsuperuser
```
After running the commands in the heroku console, your application should be synced and your frontend properly rendered!  Remember to add content by navigating to http://yournewapp.herokuapp.com/admin and use the newly created credentials to securely connect to your django-admin portal :D




