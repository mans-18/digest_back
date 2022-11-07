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

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/


ALLOWED_HOSTS = [
'''
After adding the 2 hosts below, CORS error went off. But after commenting all except the last
(required to prevent a 400 bad request). UOL HOST problem??? Firebase problem ???
'''

  #  'https://digestback.herokuapp.com/auth/',
  #  'digestback.herokuapp.com/auth',
  #  'digest.com.br',
  #  'www.digest.com.br',
  #  'hhtp://digest.com.br',
  #  'http://www.digest.com.br',
  #  'hhtps://digest.com.br',
  #  'https://www.digest.com.br',
    # DigestLa ap on firebase
  #  'digest-8d0a6.web.app',
  #  'digest-8d0a6.firebaseapp.com',
    # Digest app on firebase
  #  'digest-865d1.web.app',
  #  'digest-865d1.firebaseapp.com',
    'localhost',
    '127.0.0.1',
    'digestback.herokuapp.com',
]

#SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

#SECRET_KEY = os.environ['SECRET_KEY']
SECRET_KEY='h%$7j91w!qrkc=ve+0g#^vz)x=n-9@-b70fs@6a*fb$m9^4mxx'

# Application definition

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


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': 'dig',
#         'USER': 'postgres',
#         'PASSWORD': 'leugim2020',
#         'HOST': 'localhost',
#         'PORT': '5433',
#     }
# }

default_dburl = 'sqlite:///' + os.path.join(BASE_DIR, 'db.sqlite3')

DATABASES = {'default': config('DATABASE_URL', default=default_dburl, cast=dburl)}

#DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)


CORS_ORIGIN_ALLOW_ALL = True

# CORS_ORIGIN_WHITELIST = [
#     "http://localhost:4200"
# ]


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_L10N = True

#USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

#STATICFILES_DIRS = [
#    os.path.join(BASE_DIR, "static"),
#    'templates/css/',
#    'templates/js/',
#    'packages/core/',
#    'packages/daygrid/',
#    'packages/timegrid/',
#    'packages/list/',
#    'packages/interaction/',
#    'packages/core/locales/',
#    'css/',
#    'js/',
#]

# STATIC_ROOT = '/Users/Miguel/Projetos/digest/digproj/persona/static/'

AUTH_USER_MODEL = 'core.User'

# MEDIA_URL = '/endopic/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'endopic')

#### To send email
#### Days with an 500 internal error/smtplib.SMTPNotSupportedError: SMTP AUTH extension not supported by server
#### The problem was simply a typo: EMAIL_USER_TLS instead of _USE_
EMAIL_USE_TLS = True
# EMAIL_USE_SSL = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_PASSWORD = 'euuncpixoyhkzmdn' #'leugim@13'
EMAIL_HOST_USER = 'miguel.sza@gmail.com'
EMAIL_PORT = 587
# EMAIL_PORT = 465
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

# Compress static files for serving
# https://warehouse.python.org/project/whitenoise
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'