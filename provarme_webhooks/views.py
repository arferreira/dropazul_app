import json


from django.views.generic import View
from django.shortcuts import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from provarme_dashboard.customer.models import Customer, CustomerAddress
from provarme_dashboard.order.models import Order
from provarme_dashboard.checkout.models import Checkout


class OrderWebhook(View):

    @method_decorator([csrf_exempt])
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        body = json.loads(self.request.body)
        customer = Customer.objects.get_or_create_customer(body['customer'])
        CustomerAddress.objects.get_or_create_customer_address(customer, body['customer']['default_address'])
        order = Order.objects.get_or_create_order(customer, body)
        if order.financial_status=='paid':
            Checkout.objects.filter(cart_token==order.body['cart_token']).update(status=True)

        return HttpResponse()



class CheckoutWebhook(View):

    @method_decorator([csrf_exempt])
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        body = json.loads(self.request.body)
        customer = None
        if body.get('customer'):
            customer = Customer.objects.get_or_create_customer(body['customer'])
            CustomerAddress.objects.get_or_create_customer_address(customer, body['customer']['default_address'])        

        
        Checkout.objects.get_or_create_checkout(customer, body)

        return HttpResponse()
