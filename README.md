# Tours-and-Travels-Web-app


<!-- py -m pip install --user virtualenv
py -m venv test --> 

py -m pip install django

py -m django --version

mkdir projects
py -m django startproject YOUR_PROJECT_NAME

cd faiz






'DIRS': [os.path.join(BASE_DIR,'templates')], = settings

django template langauge or jinja
settings
py manage.py collectstatic

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'YOUR_PROJECT_NAME/static')
]

 {%block content %}

    {% endblock %}

https://pypi.org/project/psycopg2/
py -m pip install pillow
py -m pip install pymysql 
py -m pip install cryptography 

 'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'faiz',
        
        'USER': 'root',
        'PASSWORD':'',
        'HOST': 'localhost',
        'PORT':'3306'
    }
    'faiz' = YOUR_DATABASE_NAME 
  give your mysql password  

in faiz/settings.py give your email id and password and make sure it is Dont forgot to allow access in google account ---->   accounts.google.com-->security->less secure app -->allow  this for sending verification mail

py manage.py makemigrations
py manage.py sqlmigrate travello 0001

py manage.py migrate

py manage.py createsuperuser

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')

 py manage.py startapp accounts

py -m pip install windows-curses

py manage.py runserver   
 to run the project use above command 
