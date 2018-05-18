from django.urls import path, include

from atrix_landing.views import home

urlpatterns = [
    # root route
    path('', home),
]