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


