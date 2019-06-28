import re

from django.db import models
from django.contrib.postgres.fields import JSONField

from provarme_dashboard.core.models import AbstractBaseModel
from provarme_dashboard.customer.manager import CustomerManager, CustomerAddressManager


class Customer(AbstractBaseModel):

    shopify_id = models.CharField('ID Shopify', max_length=50)

    email = models.EmailField('Email', max_length=255, null=True, blank=True)
    first_name = models.CharField('Nome', null=True, blank=True, max_length=100)
    last_name = models.CharField('Sobrenome', null=True, blank=True, max_length=100)
    body = JSONField(null=True, blank=True)

    objects = CustomerManager()

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.email


class CustomerAddress(AbstractBaseModel):

    customer = models.ForeignKey(Customer, related_name='address', on_delete=models.CASCADE)
    shopify_id = models.CharField('ID Shopify', max_length=50)

    address1 = models.CharField(max_length=255, null=True, blank=True)
    address2 = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    province = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    zip_code = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    province_code = models.CharField(max_length=255, null=True, blank=True)
    country_code = models.CharField(max_length=255, null=True, blank=True)
    country_name = models.CharField(max_length=255, null=True, blank=True)
    body = JSONField(null=True, blank=True)

    objects = CustomerAddressManager()

    class Meta:
        verbose_name = 'Endereço do Cliente'
        verbose_name_plural = 'Endereços dos Clientes'

    def clean_phone(self):
        phone = self.phone
        phone = "55" + re.sub(r'[^0-9]', '', self.phone)

        return phone

    def __str__(self):
        return self.first_name


