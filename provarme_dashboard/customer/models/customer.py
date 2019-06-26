from django.db import models
from django.contrib.postgres.fields import JSONField


import re


class CustomerManager(models.Manager):

    def get_or_create_customer(self, body):
        obj, _ = self.get_or_create(shopify_id=body['id'])
        obj.email = body['email']
        obj.first_name = body['first_name']
        obj.last_name = body['last_name']
        obj.body = body

        obj.save()

        return obj

class Customer(models.Model):

    shopify_id = models.CharField('ID Shopify', max_length=50)

    email = models.EmailField('Email', max_length=255, null=True, blank=True)
    first_name = models.CharField('Nome', null=True, blank=True, max_length=100)
    last_name = models.CharField('Sobrenome', null=True, blank=True, max_length=100)
    

    body = JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Modificado em')

    objects = CustomerManager()

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

    def __str__(self):
        return self.email


class CustomerAddressManager(models.Manager):

    def get_or_create_customer_address(self, customer, body):
        obj, _ = self.get_or_create(customer=customer, shopify_id=body['id'])
        obj.address1 = body['address1']
        obj.address2 = body['address2']
        obj.city = body['city']
        obj.province = body['province']
        obj.country = body['country']
        obj.zip_code = body['zip']
        obj.phone = body['phone']
        obj.name = body['name']
        obj.province_code = body['province_code']
        obj.country_code = body['country_code']
        obj.country_name = body['country_name']
        obj.body = body

        obj.save()

        return obj


class CustomerAddress(models.Model):

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
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Modificado em')

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


