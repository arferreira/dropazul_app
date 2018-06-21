from django.urls import path, include

from provarme_landing.views import LandingPageView

app_name="provarme_landing"

urlpatterns = [
    # root route
    path('', LandingPageView.as_view(), name='home'),
]