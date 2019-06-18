from django.urls import path, include

from provarme_landing.views import LandingPageView
from provarme_tenant.views import (ThankPageView,
                                   PendingPageView)

app_name="provarme_landing"

urlpatterns = [
    # root route
    path('', LandingPageView.as_view(), name='home'),
    path('obrigado/', ThankPageView.as_view(), name='thank'),
    path('pendente/', PendingPageView.as_view(), name='pending'),
]