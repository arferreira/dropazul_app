import json

from django.views.generic import View
from django.shortcuts import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from provarme_dashboard.customer.models import Customer, CustomerAddress
from provarme_dashboard.order.models import Order


class OrderCreation(View):

    @method_decorator([csrf_exempt])
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        body = json.loads(self.request.body)
        customer = Customer.objects.get_or_create_customer(body['customer'])
        CustomerAddress.objects.get_or_create_customer_address(customer, body['customer']['default_address'])
        Order.objects.get_or_create_order(customer, body)

        return HttpResponse()
