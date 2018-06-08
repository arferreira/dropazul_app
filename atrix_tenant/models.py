import os

from django.core.mail import mail_admins
from django.db import models, connection
from django.utils.text import slugify
from tenant_schemas.models import TenantMixin
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Manager




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
    client = models.ForeignKey(Client, on_delete=models.CASCADE,
                             verbose_name='Inquilino', related_name='purchases')
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    status = models.IntegerField(
        'Situação', choices=PURCHASE_STATUS_CHOICES, default=0, blank=True
    )
    active_url = models.CharField(max_length=500, verbose_name='URL de ativação')
    pagseguro_redirect_url = models.URLField('url do pagseguro', max_length=255, blank=True)

    created_on = models.DateField(auto_now_add=True, verbose_name='Criado em')
    modified_on = models.DateTimeField('Modificado em', auto_now=True)

    def __str__(self):
        return self.client.name

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'


    def pagseguro_update_status(self, status):
        if status == '3':
            self.status = 1
            print('Status de compra alterado')
            mail_admins(
                'Notificação - Houve alteração em registro de pagamento',
                'O sistema acabou de receber uma atualização de pagamento',
                fail_silently=False
            )
        elif status == '7':
            print('Status de compra alterado')
            mail_admins(
                'Notificação - Houve alteração em registro de pagamento',
                'O sistema acabou de receber uma atualização de pagamento',
                fail_silently=False
            )
            self.status = 2
        self.save()



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


