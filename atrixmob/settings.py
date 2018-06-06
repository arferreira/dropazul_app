"""
    Settings Project
    __author__ = Antonio Ricardo
"""

import os

from decouple import config

from atrix_core.applist import *
from atrix_core.json_settings import get_settings
from atrix_core.databases import *
from atrix_core.mail_server import *



PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))



SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)

ADMINS = [
    ('Antonio Ricardo', 'antonioricardoarfs@atrixmob.com.br'),
    ('Mariana Rosa', 'mariana.souza@atrixmob.com.br'),
]
settings = get_settings()

ALLOWED_HOSTS = settings['SECURITY']['ALLOWED_HOSTS']


# DEBUG TOOLBAR
INTERNAL_IPS = ['127.0.0.1']

# Databases
DATABASES = settings['DB']


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


# Static amazon s3


AWS_ACCESS_KEY_ID = 'AKIAJMGGRT5DDWMHA4VQ'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'atrixmobcore'
AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'



# static files
AWS_S3_OBJECT_PARAMETERS = {
    'CacheControl': 'max-age=86400',
}
AWS_LOCATION = 'static'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# STATIC_ROOT = 'staticfiles/'
#
# STATIC_URL = '/static/'
#
# STATICFILES_DIRS = (os.path.join('static'),)



# Media
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

DEFAULT_FILE_STORAGE = 'tenant_schemas.storage.TenantFileSystemStorage'




# LOGGING do atrix

from atrix_core.logging import LOGGING


# EMAIL SMTP
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = "smtp.mailgun.org"
EMAIL_PORT = 587
EMAIL_HOST_USER = "postmaster@mg.atrixmob.com.br"
EMAIL_HOST_PASSWORD = "1ef3d0eac06689079e8d057b35f9c9ff-b892f62e-ca36ad6d"
DEFAULT_FROM_EMAIL = "contato@atrixmob.com.br"
CONTACT_EMAIL = "contato@atrixmob.com.br"
EMAIL_SUBJECT_PREFIX = '[atrixmob]'