import json
from datetime import datetime
from decimal import Decimal

from tenant_schemas.test.cases import TenantTestCase
from tenant_schemas.test.client import TenantClient

from django.urls import reverse_lazy

from provarme_dashboard.customer.models import Customer
from provarme_dashboard.order.models import Order
from provarme_webhooks.tests.fixtures import ORDER_BODY
from provarme_dashboard.core.tests.helpers import BaseTenantTestCase as TestCase


class OrderCreationTestCase(TestCase):

    def setUp(self):
        super(OrderCreationTestCase, self).setUp()
        self.headers = {
            'X-Shopify-Topic': 'orders/create',
            'X-Shopify-Hmac-Sha256': 'XWmrwMey6OsLMeiZKwP4FppHH3cmAiiJJAweH5Jo4bM=',
            'X-Shopify-Shop-Domain': 'johns-apparel.myshopify.com',
            'X-Shopify-API-Version': '2019-04',
            'HTTP_X_REQUESTED_WITH': u'XMLHttpRequest'
        }
        self.response = self.client.post(reverse_lazy('webhooks:order-creation'), data=json.dumps(ORDER_BODY),
                                         content_type='application/json', **self.headers)

        self.customer = Customer.objects.first()
        self.customer_address = self.customer.address.first()
        self.order = self.customer.orders.first()

    def test_status_code(self):
        self.assertEqual(200, self.response.status_code)

    def test_customer(self):
        expected_values = {
            'shopify_id': '115310627314723954',
            'email': 'john@test.com',
            'first_name': 'John',
            'last_name': 'Smith',
            'body': ORDER_BODY['customer'],
        }

        for key, value in expected_values.items():
            with self.subTest():
                self.assertEqual(getattr(self.customer, key), value)

    def test_customer_address(self):
        expected_values = {
            'address1': '123 Elm St.',
            'address2': None,
            'city': 'Ottawa',
            'province': 'Ontario',
            'country': 'Canada',
            'zip_code': 'K2H7A8',
            'phone': '123-123-1234',
            'name': '',
            'province_code': 'ON',
            'country_code': 'CA',
            'country_name': 'Canada',
            'body': ORDER_BODY['customer']['default_address'],
        }

        for key, value in expected_values.items():
            with self.subTest():
                self.assertEqual(getattr(self.customer_address, key), value)

    def test_order(self):
        expected_values = {
            'customer': self.customer,
            'shopify_id': '820982911946154508',
            'total_price': Decimal('403.00'),
            'financial_status': 'voided',
            'order_number': '1234',
            'body': ORDER_BODY,
        }

        for key, value in expected_values.items():
            with self.subTest():
                self.assertEqual(getattr(self.order, key), value)
