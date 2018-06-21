from django.urls import path, include

from provarme_site.views import IndexPageView

app_name="provarme_site"

urlpatterns = [
    # root route
    path('', IndexPageView.as_view(), name='index'),
]