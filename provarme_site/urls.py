from django.urls import path, include

from provarme_site.views import IndexPageView, tracking_order

app_name="provarme_site"

urlpatterns = [
    # root route
    path('', IndexPageView.as_view(), name='index'),
    path('rastreio/', tracking_order, name='tracking_order'),


]