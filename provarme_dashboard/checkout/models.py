from datetime import date

from django.db import models
from django.contrib.postgres.fields import JSONField

from provarme_dashboard.checkout.manager import CheckoutManager
from provarme_dashboard.core.models import AbstractBaseModel


class Checkout(AbstractBaseModel):

    customer = models.ForeignKey('provarme_dashboard.Customer', related_name='checkouts', on_delete=models.SET_NULL, null=True)
    shopify_id = models.CharField('ID Shopify', max_length=50)
    token = models.CharField('Token', max_length=150)
    cart_token = models.CharField('Token do Carrinho', max_length=150)
    email = models.CharField('Email', max_length=150)
    
    checkout_url = models.CharField('Url', max_length=255)

    body = JSONField(null=True, blank=True)
    status = models.BooleanField('Status', default=False)

    objects = CheckoutManager()

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Abandono'
        verbose_name_plural = 'Abandonos'

    def __str__(self):
        return self.shopify_id



