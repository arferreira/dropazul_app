from datetime import datetime
from decimal import Decimal
from model_mommy import mommy

from django.urls import reverse_lazy

from provarme_dashboard.traffic.models import Traffic
from provarme_dashboard.products.models import Product
from provarme.tests.helpers import BaseTenantTestCase as TestCase


class TrafficCreateViewTestCase(TestCase):

    def setUp(self):
        super(TrafficCreateViewTestCase, self).setUp()
        self.data = {
            'product': mommy.make(Product).pk,
            'event_date': datetime.now().date(),
            'order_quantity': 5,
            'investment': Decimal('50.00'),
        }
        self.response = self.client.post(reverse_lazy('dashboard:new_traffic'), data=self.data)

    def test_status_code(self):
        self.assertEqual(302, self.response.status_code)

    def test_url_redirect(self):
        self.assertEqual('/painel/trafego/', self.response.url)


class TrafficCreateViewWithErrorTestCase(TestCase):

    def setUp(self):
        super(TrafficCreateViewWithErrorTestCase, self).setUp()
        product = mommy.make(Product)
        today = datetime.now().date()
        mommy.make(Traffic, product=product, event_date=today)

        self.data = {
            'product': product.pk,
            'event_date': today,
            'order_quantity': 5,
            'investment': Decimal('50.00'),
        }
        self.response = self.client.post(reverse_lazy('dashboard:new_traffic'), data=self.data)

    def test_status_code(self):
        self.assertEqual(200, self.response.status_code)

    def test_object_list(self):
        self.assertDictEqual({'__all__': ['Tráfego diário com este Produto e Data já existe.']},
                             self.response.context_data['form'].errors)


class TrafficUpdateViewTestCase(TestCase):

    def setUp(self):
        super(TrafficUpdateViewTestCase, self).setUp()
        self.traffic = mommy.make(Traffic)
        self.product = mommy.make(Product)
        self.data = {
            'product': self.product.pk,
            'event_date': datetime.now().date(),
            'order_quantity': 5,
            'investment': Decimal('50.00'),
        }
        self.response = self.client.post(reverse_lazy('dashboard:update_traffic', args=[self.traffic.pk]),
                                         data=self.data)
        self.traffic = Traffic.objects.first()

    def test_status_code(self):
        self.assertEqual(302, self.response.status_code)

    def test_url_redirect(self):
        self.assertEqual('/painel/trafego/', self.response.url)

    def test_object_field_updated(self):
        self.data['product'] = self.product

        for key, value in self.data.items():
            with self.subTest():
                self.assertEqual(getattr(self.traffic, key), value)


class TrafficListViewTestCase(TestCase):

    def setUp(self):
        super(TrafficListViewTestCase, self).setUp()
        mommy.make(Traffic, _quantity=10)
        self.response = self.client.get(reverse_lazy('dashboard:traffic'))

    def test_status_code(self):
        self.assertEqual(200, self.response.status_code)

    def test_object_list(self):
        self.assertEqual(10, len(self.response.context_data['object_list']))
