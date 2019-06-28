from django.urls import path

from provarme_webhooks.views import OrderCreation


app_name="provarme_webhooks"

urlpatterns = [
    path('order/creation/', OrderCreation.as_view(), name='order-creation'),
    path('checkout/creation/', OrderCreation.as_view(), name='order-creation'),
]
