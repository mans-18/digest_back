"""
Django settings for digproj project.

Generated by 'django-admin startproject' using Django 2.2.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os
import dj_database_url
from decouple import config
from dj_database_url import parse as dburl

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')


ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'localhost:4200',
    'digestback.herokuapp.com',
    'https://digestback.herokuapp.com/api/persona/email/',
    'digest.com.br',
    'https://digest.com.br',
    'https://www.digest.com.br',
]

DEBUG = True #config('DEBUG', default=False, cast=bool)

SECRET_KEY = os.environ.get('SECRET_KEY')

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'rest_framework.authtoken',
    'corsheaders',
    'core',
    'django_filters',
    'user',
    'persona',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'digproj.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates'),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'digproj.wsgi.application'


### Required to deploy
default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = {'default': config('DATABASE_URL', default=default_dburl, cast=dburl)}

#DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

CORS_ORIGIN_ALLOW_ALL = True

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME':
        'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME':
        'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'pt-br'

#TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'


AUTH_USER_MODEL = 'core.User'

EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
#EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
#EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD_LOCAL']
#EMAIL_HOST_PASSWORD = os.environ['EMAIL_HOST_PASSWORD'] # APP PSW FOR DIGEST.COM.BR

###### ANOTHER WAY  ########
#EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD_LOCAL')
#EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD_HEROKU')

EMAIL_HOST_USER = 'miguel.sza@gmail.com'
EMAIL_PORT = 587
# EMAIL_PORT = 465
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Compress static files for serving
# https://warehouse.python.org/project/whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'