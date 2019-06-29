from django.urls import path

from provarme_webhooks.views import OrderWebhook, CheckoutWebhook


app_name="provarme_webhooks"

urlpatterns = [
    path('order/', OrderWebhook.as_view(), name='order'),
    path('checkout/', CheckoutWebhook.as_view(), name='checkout'),
]
