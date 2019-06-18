import os
from datetime import timedelta

from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import mail_admins, send_mail
from django.db import models, connection
from django.template.loader import render_to_string
from django.utils.datetime_safe import datetime
from django.utils.text import slugify
from tenant_schemas.models import TenantMixin
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Manager


from tenant_schemas.utils import schema_exists, schema_context, connection

from provarme_tenant.tokens import account_activation_token


class Plan(models.Model):
    name = models.CharField(max_length=500, verbose_name='Nome')
    description = models.CharField(max_length=500, verbose_name='Descrição')
    amount = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Preço')
    is_active = models.BooleanField(default=True, verbose_name='Ativo?')
    created_on = models.DateField(auto_now_add=True, verbose_name='Criado em')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Plano'
        verbose_name_plural = 'Planos'




class Client(TenantMixin):
    # Dados pessoais
    name = models.CharField(max_length=500, verbose_name='Nome')
    name_fantasy = models.CharField(max_length=500, verbose_name='Nome de Fantasia')
    document = models.CharField(max_length=20, blank=True, null=True, verbose_name="CNPJ ou CPF")
    phone_number = models.CharField(max_length=20, blank=False, null=False, verbose_name="Número de Telefone")
    # Dados de Endereço
    zipcode = models.CharField(max_length=10, blank=True, null=True, verbose_name="CEP")

    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="Cidade")

    province = models.CharField(max_length=100, blank=True, null=True, verbose_name="Estado/Província")

    address = models.CharField(max_length=100, blank=True, null=True, default='', verbose_name="Endereço")

    address_number = models.CharField(max_length=20, blank=True, null=True, default='', verbose_name="Número")

    neighborhood = models.CharField(max_length=100, blank=True, null=True, default='', verbose_name="Bairro")
    # Dados de contratação
    acceptance = models.BooleanField(default=False, verbose_name='Aceito os termos')
    is_active = models.BooleanField(default=False, verbose_name='Ativo?')
    display_site = models.BooleanField(default=False)
    display_landing = models.BooleanField(default=False)
    created_on = models.DateField(auto_now_add=True)

    # automaticamente o sistema criara as migraçoes a cada tenant criado
    auto_create_schema = True


    def __str__(self):
        return '%s' % self.name_fantasy

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


PURCHASE_STATUS_CHOICES = (
    (0, 'Pendente'),
    (1, 'Pago'),
    (2, 'Cancelado'),
)


class Purchase(models.Model):
    cod_product = models.IntegerField('ID do produto', null=True)
    purchase_date = models.DateField('Data da Compra', auto_now_add=True, null=True)
    prod_name = models.CharField(max_length=255, verbose_name='Nome do produto', null=True)
    transaction = models.IntegerField('ID da da venda', default=0, null=True)
    email = models.CharField('Email do Comprador', max_length=255, null=True)
    first_name = models.CharField('Primeiro Nome', max_length=100, null=True)
    last_name = models.CharField('Último Nome', max_length=100, null=True)
    cpf = models.CharField('CPF', max_length=11, null=True)
    phone_local_code = models.CharField('DDD', max_length=3, null=True)
    phone_number = models.CharField('Telefone', max_length=9, null=True)
    payment_type = models.CharField('Tipo', max_length=100, null=True)
    status = models.CharField('Situação', max_length=100, null=True)


    def __str__(self):
        return self.client.first_name

    class Meta:
        ordering = ['-purchase_date']
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'








class Profile(models.Model):
    def image_path(self, filename):
        extension = os.path.splitext(filename)[1][1:]
        file_name = os.path.splitext(filename)[0]
        url = "%s/Users/%s/profile/%s.%s" % (
        connection.tenant.domain_url, self.user.id, slugify(str(file_name)), extension)
        return url

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    cellphone = models.CharField(max_length=20)
    # Dados empresariais
    cnpj = models.CharField(max_length=40)
    cpf = models.CharField(max_length=40)
    image_profile = models.ImageField(upload_to=image_path, null=True, blank=True)


    def __str__(self):
        return self.user.get_full_name()



# ============================================================
# Conectamos os signals
# ============================================================

from .signals import *


