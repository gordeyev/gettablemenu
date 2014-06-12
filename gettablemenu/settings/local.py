from .base import *

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'gettablemenu',
        'USER': 'mikhail',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}