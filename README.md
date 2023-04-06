# Scoreboard Django API 



## Setup
--- 

This application was built using Django 4.17, but you may also use Django 4.2.
Python 3.8 and above is required for Django 4
```
pip install Django==4.2
```

We are also using Postgres 13 for the database, but you may try with newer versions.

These are the expected environment variables.

```
export DJANGO_SECRET='your django secret'
export HOST_ENV='localhost'
export DEBUG=True

# Database
export DBUSER='your db user'
export DBPASSWORD='your db password'
export DBNAME='your db name'
export DBHOST='your db host or 127.0.0.1'
```

You may install the required libraries using requirements.txt:
Remember to use a virtual env if you want to download the libraries separately!
```
pip install -r requirements.txt
```

Don't forget to make migrations and migrate!
```
python manage.py makemigrations
python manage.py migrate
```

Finally, run the server!
```
python manage.py runserver
```

If you would like to run the testcases, you may use:
```
python manage.py test
```
