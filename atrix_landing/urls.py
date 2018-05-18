from django.urls import path, include

from atrix_landing.views import LandingPageView

urlpatterns = [
    # root route
    path('', LandingPageView.as_view()),
]