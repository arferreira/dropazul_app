from django.contrib import admin
from django.urls import path, include

from atrix_landing import urls as atrix_landing_urls

urlpatterns = [
    # root route
    path('', include(atrix_landing_urls)),
    # admin django route
    path('admin/', admin.site.urls),
]
