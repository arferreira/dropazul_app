from django.urls import path, include

from atrix_landing.views import LandingPageView

app_name="atrix_landing"

urlpatterns = [
    # root route
    path('', LandingPageView.as_view(), name='home'),
]