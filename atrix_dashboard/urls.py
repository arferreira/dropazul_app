from django.urls import path, include

from atrix_dashboard.views import IndexView

app_name="atrix_dashboard"

urlpatterns = [
    # root route
    path('', IndexView.as_view(), name='index'),
]