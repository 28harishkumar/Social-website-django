
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

DEBUG = True

TEMPLATE_DEBUG = True

SECRET_KEY = 'secret_key'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {

    'default':{
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'database',
        'USER':'user',
        'PASSWORD':'password',
        'HOST':'127.0.0.1',
        'PORT': '3306',
        },
    
}









