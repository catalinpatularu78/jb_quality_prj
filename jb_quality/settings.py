"""
Django settings for jb_quality project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

import os

import django_heroku
import dj_database_url


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'django-insecure-lp-(ja5oo9(-ah3*u%*kac!g5p(sl#+rypm@qhiv1p90e6r(@b'
SECRET_KEY = os.environ.get('SECRET_KEY', 'changeme')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#DEBUG = bool(int(os.environ.get('DEBUG', 0)))

#ALLOWED_HOSTS = ['127.0.0.1', 'jbdjangoapp.herokuapp.com', 'http://jbmanufacturingtests.herokuapp.com/']

#ALLOWED_HOSTS = ['127.0.0.1','jbmanufacturingtests.herokuapp.com']

#ALLOWED_HOSTS = ['.localhost', '127.0.0.1', '[::1]']
ALLOWED_HOSTS = ['*']
# ALLOWED_HOSTS_ENV = os.environ.get('ALLOWED_HOSTS')


# if ALLOWED_HOSTS_ENV:
#     ALLOWED_HOSTS.extend(ALLOWED_HOSTS_ENV.split(','))
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',
    'django_filters',
    'django_cleanup.apps.CleanupConfig',
    #'dashboard.apps.DashboardConfig', # Dashboard app added
    'dashboard'
    
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',   
    'whitenoise.middleware.WhiteNoiseMiddleware',  
]

ROOT_URLCONF = 'jb_quality.urls'


TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            
            BASE_DIR / "templates"
            
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.media',
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

            ],
        },
    },
]

WSGI_APPLICATION = 'jb_quality.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }


#heroku app credentials (Conor)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'df3iogc6kqm1t8',
        'USER': 'ykykmwpsnncxna',
        'PASSWORD': '1319e9ceae205af0c3047cf7e73ee86fbfdf25377dec4d1efa7ce575b9c272b3',
        'HOST': 'ec2-34-239-241-121.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}

db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/


USE_L10N = False

DATE_INPUT_FORMATS = [
    "%d/%m/%Y",
    '%Y-%m-%d'
]

DATETIME_INPUT_FORMATS = [
    '%d/%m/%Y %H:%i'
]

DATETIME_FORMAT="d/m/Y H:i"

DATE_FORMAT = "d/m/Y"

LANGUAGE_CODE = 'en-GB'

TIME_ZONE = 'Europe/Dublin'

USE_I18N = True

USE_TZ = True


LOGIN_URL = 'login'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/


# STATIC_URL = '/static/'

# STATICFILES_DIRS = [
#     BASE_DIR / "static",
# ]




# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



# Debugging in heroku live
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': ('%(asctime)s [%(process)d] [%(levelname)s] ' +
                        'pathname=%(pathname)s lineno=%(lineno)s ' +
                        'funcname=%(funcName)s %(message)s'),
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        }
    },
    'handlers': {
        'null': {
            'level': 'DEBUG',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'testlogger': {
            'handlers': ['console'],
            'level': 'INFO',
        }
    }
}

DEBUG_PROPAGATE_EXCEPTIONS = True
COMPRESS_ENABLED = os.environ.get('COMPRESS_ENABLED', False)


# Email functionality TEST - NOT FOR PRODUCTION 
# seperate credentials when going to production  
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.office365.com' #smtp.office365.com #smtp-mail.outlook.com
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'jbdjango@outlook.com'
EMAIL_HOST_PASSWORD = 'JBengineering'


#MEDIA_ROOT = os.path.join(BASE_DIR, 'media/') # the path becomes [project dir]\media\
#DISABLE_SERVER_SIDE_CURSORS = True


STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static/'),)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/' #/static here is the proxy and it will serve both static and media files
STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles') #the static root tells the container where it expects the static files to be stored
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

''' Django docker deployment walkthrough https://www.youtube.com/watch?v=nh1ynJGJuT8 '''

# MEDIA_URL = '/static/media/' #/static here is the proxy and it will serve both static and media files
# STATIC_URL = '/static/static/'

# STATIC_ROOT = '/vol/web/static' #the static root tells the container where it expects the static files to be stored
# MEDIA_ROOT = '/vol/web/media'

django_heroku.settings(locals() ) #staticfiles=False


# VALID_IMAGE_EXTENSIONS = [
#     ".jpg",
#     ".jpeg",
#     ".png",
#     ".gif",
# ]

# def valid_url_extension(url, extension_list=VALID_IMAGE_EXTENSIONS):

#     return any([url.endswith(e) for e in extension_list])

