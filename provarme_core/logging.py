import os

from provarme.settings import BASE_DIR
from .json_settings import get_settings
from django.conf import settings

settings = get_settings()

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'tenant_context': {
            'format': '[%(schema_name)s:%(domain_url)s] '
                      '%(levelname)-7s %(asctime)s %(message)s',
        },
    },
    'filters': {
        'tenant_context': {
            '()': 'tenant_schemas.log.TenantContextFilter'
        },
    },
    'handlers': {
        'debug_file': {
            'level': 'DEBUG',
            'filters': ['tenant_context'],
            'class': 'logging.FileHandler',
            'filename': settings["LOGGING"]["DEBUG_PATH"],
            'formatter': 'tenant_context'
        },
        'error_file': {
            'level': 'ERROR',
            'filters': ['tenant_context'],
            'class': 'logging.FileHandler',
            'filename': settings["LOGGING"]["ERROR_PATH"],
            'formatter': 'tenant_context'
        },
        'logfile': {
            'level':'DEBUG',
            'filters': ['tenant_context'],
            'class':'logging.handlers.RotatingFileHandler',
            'filename': os.path.join(BASE_DIR, 'django.log'),
            'maxBytes': 1024*1024*5, # 5MB
            'backupCount': 0,
            'formatter': 'tenant_context',
        },
        'console': {
            'level': 'DEBUG',
            'filters': ['tenant_context'],
            'class': 'logging.StreamHandler',
            'formatter': 'tenant_context',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'error_file'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['debug_file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'provarme': {
            'handlers': ['console', 'logfile'],
            'level': 'DEBUG',
            'propagate': True,
        }
    },
}
