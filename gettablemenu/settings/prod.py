from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {}

DATABASES['default'] = dj_database_url.config()