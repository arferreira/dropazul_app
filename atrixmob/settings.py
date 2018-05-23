"""
    Settings Project
    __author__ = Antonio Ricardo
"""

import os

from decouple import config

from atrix_core.internationalization import *
from atrix_core.applist import *
from atrix_core.json_settings import get_settings_development, get_settings_production
from atrix_core.databases import *
from atrix_core.mail_server import *
from atrix_core.logging import *

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


DEBUG = True

settings_development = get_settings_development()
settings_production = get_settings_production()

SECRET_KEY = settings_production['SECRET_KEY']


if DEBUG:
    ALLOWED_HOSTS = settings_development['SECURITY']['ALLOWED_HOSTS']
else:
    ALLOWED_HOSTS = settings_production['SECURITY']['ALLOWED_HOSTS']


# DEBUG TOOLBAR
INTERNAL_IPS = ['127.0.0.1']

# Databases
if DEBUG:
    DATABASES = settings_development['DB']
else:
    DATABASES = settings_production['DB']


MIDDLEWARE = [
    # Tenant schemas multi tenancy
    'tenant_schemas.middleware.TenantMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


ROOT_URLCONF = 'atrixmob.urls'
PUBLIC_SCHEMA_URLCONF  =  'atrixmob.urls_public'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'atrixmob.wsgi.application'




AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.' +
        'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.' +
        'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.' +
        'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.' +
        'NumericPasswordValidator',
    },
]


TENANT_MODEL = 'atrix_tenant.Client'

# Arquivos estaticos


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

MEDIA_URL = '/media/'
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
STATICFILES_DIRS = (os.path.join(BASE_DIR, "static"), )
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
DEFAULT_FILE_STORAGE = 'tenant_schemas.storage.TenantFileSystemStorage'



# Email

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'antonio.eschola@gmail.com'
EMAIL_HOST_PASSWORD = 'adsl5419'
EMAIL_PORT = 587


try:
    from local_settings import *
except ImportError:
    pass