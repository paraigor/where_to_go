# Where to go — Moscow through Artyom's eyes
 
Website about most interesting places in Moscow. Artyom's author's project.  
Based on Django ORM system.

### [View demo](https://skir.pythonanywhere.com/)

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
$ py manage.py runserver
```

Check [this](https://docs.djangoproject.com/en/5.0/howto/deployment/) article for project deployment.

## Usage

View locally started web site, go to [http://127.0.0.1:8000](http://127.0.0.1:8000).

Django admin site available at [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin).  
New places can be added here.  
Also new places can be added from JSON file by management command:
```
$ py manage.py load_place http://example.com/place.json
- or -
$ py manage.py load_place path/to/place.json
```

Place's photos can be sorted at place's admin page. First photo used as main place photo at frontend page.

Some details about place can be fetched in JSON format at `http://127.0.0.1:8000/places/<place_id>`.

Example of JSON file:
```
{
    "title": "Экскурсионный проект «Крыши24.рф»",
    "imgs": [
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/af7b8599fec9d2542a011f1d01d459e2.jpg",
        "https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/media/965c5a3ff5b2431e646d30b6744afd2d.jpg",
    ],
    "description_short": "Хотите увидеть Москву с высоты и разделить яркие ...",
    "description_long": "<p>Проект «Крыши24.рф» проводит экскурсии и меро... </p>",
    "coordinates": {
        "lng": "37.32478399999957",
        "lat": "55.70731600000015"
    }
}
```

## Project Goals
The code is written for educational purposes on online-course for web-developers dvmn.org.
