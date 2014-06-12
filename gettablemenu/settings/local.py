from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

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