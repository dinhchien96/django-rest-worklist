# Django Rest Framework API TODO LIST

-This is a simple example of a REST API using DjangoTemplates.

-In this project I will use sqlite to save data.

## Installation

    python 3.6 +
    django >=4.0.0, <4.1.0
    djangorestframework
    djangorestframework-simplejwt

## How to run the application

Installation using pip:

    pip install -r requirements.txt


Migrations data:

    python manage.py makemigrations
    python manage.py migrate


Run server:

    cd work_list
    python manage.py runserver #this server will run with port 8000

## Post-man

Using <a href='https://www.postman.com/'>post man</a> application to check api

Import file Django.postman_collection.json into your postman application to get my curl 

![plot](./image/postman.png)