from django.contrib import admin
from django.urls import path, include

# url para a landing page
from atrix_landing import urls as landing_urls

urlpatterns = [
    # root route - Landing page
    path('', include(landing_urls, namespace='landing-page')),
    # admin django route
    path('admin/', admin.site.urls),
]
