from django.urls import path, include

from atrix_site.views import IndexPageView

app_name="atrix_site"

urlpatterns = [
    # root route
    path('', IndexPageView.as_view(), name='index'),
]