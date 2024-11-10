# Where to go — Moscow through Artyom's eyes
 
Website about most interesting places in Moscow. Artyom's author's project.  
Based on Django ORM system.

## Installation

Python3 should already be installed. Version 3.11.* recommended.
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

Security sensitive information highly recommended to store in environmental variables.  
Example of `.env` file for development environment:
```
DJANGO_SECRET_KEY = "xxxXXXxxxXXXXxxxx"
DJANGO_DEBUG = True
ALLOWED_HOSTS = .localhost,127.0.0.1,[::1]
DATABASE_URL = sqlite:///db.sqlite3

CSRF_COOKIE_SECURE = False
SESSION_COOKIE_SECURE = False
SECURE_SSL_REDIRECT = False
SECURE_HSTS_INCLUDE_SUBDOMAINS = False
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_PRELOAD = False
```

Make initial migrations:
```
$ py manage.py migrate
```
Create admin user:
```
$ py manage.py createsuperuser
```
Start Django local web server:
```
py manage.py runserver
```

Check [this](https://docs.djangoproject.com/en/5.0/howto/deployment/) article for project deployment.

## Usage

View locally started web site, go to [http://127.0.0.1:8000](http://127.0.0.1:8000).

Django admin site available at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).  
New places can be added here.  
Place's photos can be sorted at place's admin page. First photo used as main place photo at frontend page.

Some details about place can be fetched in JSON format at `http://127.0.0.1:8000/places/<place_id>`.

## Project Goals
The code is written for educational purposes on online-course for web-developers dvmn.org.
