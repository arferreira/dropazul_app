import os

from django.db import models, connection
from django.utils.text import slugify
from tenant_schemas.models import TenantMixin
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models import Manager


from pagseguro.api import PagSeguroItem, PagSeguroApi


from .exceptions import CheckoutException


class PurchaseManager(Manager):
    def create_purchase(self, cart):
        return self.create(user=cart.user, cart=cart, price=cart.price)

    def create_checkout(self, cart):
        purchase = self.create_purchase(cart)
        pagseguro_api = PagSeguroApi(reference=str(purchase.id))
        for cart_item in cart.cart_items.all():
            ticket = cart_item.ticket
            item = PagSeguroItem(
                id=str(ticket.id),
                description=ticket.title,
                amount=str(cart_item.unit_price),
                quantity=cart_item.quantity
            )
            pagseguro_api.add_item(item)
        pagseguro_data = pagseguro_api.checkout()
        if pagseguro_data['success'] is False:
            raise CheckoutException(pagseguro_data['message'])
        purchase.pagseguro_redirect_url = pagseguro_data['redirect_url']
        purchase.save()
        cart.closed = True
        cart.save()
        return purchase

    def update_purchase_status(self, pagseguro_transaction):
        status_map = {
            '3': 'paid',
            '7': 'canceled'
        }
        purchase = self.filter(id=pagseguro_transaction['reference']).first()
        if not purchase:
            return
        if pagseguro_transaction['status'] not in ('3', '7'):
            return purchase
        purchase.status = status_map[pagseguro_transaction['status']]
        purchase.save()
        return purchase


class Plan(models.Model):
    name = models.CharField(max_length=500, verbose_name='Nome')
    description = models.CharField(max_length=500, verbose_name='Descrição')
    amount = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='Preço')
    is_active = models.BooleanField(default=True)
    created_on = models.DateField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Plano'
        verbose_name_plural = 'Planos'



PURCHASE_STATUS_CHOICES = (
    ('pending', 'Pendente'),
    ('paid', 'Pago'),
    ('canceled', 'Cancelado'),
)


class Purchase(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,
                             verbose_name='usuário', related_name='purchases')
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    status = models.CharField('status da compra', max_length=16, default='pending',
                              choices=PURCHASE_STATUS_CHOICES)
    pagseguro_redirect_url = models.URLField('url do pagseguro', max_length=255, blank=True)
    created_on = models.DateField(auto_now_add=True)
    objects = PurchaseManager()

    def __str__(self):
        return str(self.id)

    class Meta:
        ordering = ['-created_on']
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'




class Client(TenantMixin):
    name = models.CharField(max_length=500, verbose_name='Nome')
    name_fantasy = models.CharField(max_length=500, verbose_name='Nome de Fantasia')
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE, default=1, verbose_name='Plano contratado')
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


