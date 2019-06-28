from datetime import date

from django.db import models
from django.contrib.postgres.fields import JSONField

from provarme_dashboard.order.manager import OrderManager
from provarme_dashboard.core.models import AbstractBaseModel


class Order(AbstractBaseModel):

    customer = models.ForeignKey('provarme_dashboard.Customer', related_name='orders', on_delete=models.CASCADE)
    shopify_id = models.CharField('ID Shopify', max_length=50)

    total_price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    financial_status = models.CharField(max_length=255, null=True, blank=True)
    order_number = models.CharField(max_length=255, null=True, blank=True)
    body = JSONField(null=True, blank=True)

    objects = OrderManager()

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return self.shopify_id



