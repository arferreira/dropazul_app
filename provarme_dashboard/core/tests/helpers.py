from model_mommy import mommy

from django.urls import reverse_lazy

from tenant_schemas.test.cases import TenantTestCase
from tenant_schemas.test.client import TenantClient


class BaseTenantTestCase(TenantTestCase):

    def setUp(self):
        self.client = TenantClient(self.tenant)

        self.user = mommy.make('auth.User', email='test@test.com')
        self.user.set_password('123456')
        self.user.save()

        self.client.post(reverse_lazy('tenant:login'), {'email': self.user.email, 'password': '123456'})

        mommy.make('provarme_dashboard.Setup', tx_shopify=1, tx_gateway=1, tx_antecipation=1, tx_tax=1, tx_iof=1,
                   tx_cashback=1,)
