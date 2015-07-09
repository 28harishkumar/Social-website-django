import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

DEBUG = False

TEMPLATE_DEBUG = DEBUG

SECRET_KEY = 'your_secret_key'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {

    'default':{
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'database_name',
        'USER':'username',
        'PASSWORD':'password',
        'HOST':'host_name',
        'PORT': '5432',
        },
    
}

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers
ALLOWED_HOSTS = ['*']

# Static asset configuration
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
