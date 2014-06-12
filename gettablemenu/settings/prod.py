from .base import *

import dj_database_url
from unipath import Path


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

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

DATABASES['default'] = dj_database_url.config()

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'gettablemenu.herokuapp.com']

PROJECT_DIR = str(Path(__file__).ancestor(2))

STATICFILES_DIRS = (
	os.path.join(BASE_DIR, "menu/static/"),
	os.path.join(PROJECT_DIR, "menu/static/"),
	'/var/www/static/',
)