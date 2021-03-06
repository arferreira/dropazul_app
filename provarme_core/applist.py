BEFORE_DJANGO_APPS = (
    'tenant_schemas',
)

DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.humanize',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'widget_tweaks',
    'debug_toolbar',
    'pagseguro',
)

LOCAL_APPS = (
    'provarme_tenant',
    'provarme_landing',
    'provarme_dashboard',
    'provarme_dashboard.store',
)

THIRD_PARTY_APPS = (
    'solo',
    'storages',
    'test_without_migrations',
)

SHARED_APPS = (
    'tenant_schemas',
    'provarme_tenant',
) + DJANGO_APPS

TENANT_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
) + LOCAL_APPS

INSTALLED_APPS = BEFORE_DJANGO_APPS + DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS
