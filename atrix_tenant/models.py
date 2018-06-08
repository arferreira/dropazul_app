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

from atrix_tenant.tokens import account_activation_token


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

    created_on = models.DateField(auto_now_add=True, verbose_name='Criado em')
    modified_on = models.DateTimeField('Modificado em', auto_now=True)
    validate_on = models.DateTimeField(default=datetime.now()+timedelta(days=30), verbose_name='Valido até')

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
            client = Client.objects.get(pk=self.client.pk) # recuperando o tenant para notificação.
            # preparando para disparar a notificação
            with schema_context(client.schema_name):
                mail_subject = '[atrixmob] - Bem-vindo ao AtrixMob! Segue seus dados de acesso.'
                user = User.objects.last()
                to_email = user.email
                plain_text = render_to_string('atrix_tenant/email_notification/tenant_active_email.html', {
                    'user': user,
                    'domain': self.active_url,
                    'id': user.pk,
                    'token': account_activation_token.make_token(user),
                })
                message_html = render_to_string('atrix_tenant/email_notification/tenant_active_email.html', {
                    'user': user,
                    'domain': self.active_url,
                    'id': user.pk,
                    'token': account_activation_token.make_token(user),
                })
                try:
                    send_mail(
                        mail_subject,
                        plain_text,
                        'contato.atrixmob@atrixmob.com.br',
                        [to_email],
                        html_message=message_html,
                        fail_silently=False
                    )
                except Exception as e:
                    print('O email não foi enviado, erro: ', e)
                mail_admins(
                    'Notificação - Houve alteração em registro de pagamento',
                    'O sistema acabou de receber uma atualização de pagamento do:  %s' % client,
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


