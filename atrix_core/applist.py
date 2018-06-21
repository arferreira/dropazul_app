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
    'atrix_tenant',
    'atrix_landing',
    'atrix_dashboard',
    'atrix_dashboard.customer',
    'atrix_dashboard.employee',
    'atrix_dashboard.person',
    'atrix_dashboard.product',
    'atrix_dashboard.provider',
    'atrix_dashboard.service',
)

THIRD_PARTY_APPS = (
    'solo',
    'storages',
)

SHARED_APPS = (
    'tenant_schemas',
    'atrix_tenant',
) + DJANGO_APPS

TENANT_APPS = (
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
) + LOCAL_APPS

INSTALLED_APPS = BEFORE_DJANGO_APPS + DJANGO_APPS + LOCAL_APPS + THIRD_PARTY_APPS
