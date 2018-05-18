from django.contrib import admin
from django.urls import path, include

from atrix_landing import urls

urlpatterns = [
    # root route
    path('', include(urls)),
    # admin django route
    path('admin/', admin.site.urls),
]
