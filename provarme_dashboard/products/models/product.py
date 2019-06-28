from django.db import models

from provarme_dashboard.setups.models import Setup
from provarme_dashboard.providers.models.provider import Provider


class Product(models.Model):

    STATUS = (
        (True, 'Ativa'),
        (False, 'Inativa'),
    )

    name = models.CharField('Nome', max_length=255)
    slug = models.SlugField('Apelido', max_length=40)
    link = models.CharField('Link para o Produto', max_length=255)
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    cost = models.DecimalField('Custo do Produto', max_digits=5, decimal_places=2)
    markup = models.DecimalField('Markup', max_digits=3, decimal_places=2)
    marketing = models.IntegerField('Custo com Marketing', default=20)

    recommended_price = models.DecimalField('Preço recomendado', max_digits=5, decimal_places=2)
    price = models.DecimalField('Preço Final', max_digits=5, decimal_places=2)
    status = models.BooleanField(verbose_name='Situação', default=True, choices=STATUS)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Modificado em')

    @property
    def final_cost(self):
        setup = Setup.objects.first()

        return round(((self.cost * setup.tx_iof) +
                ((self.price * setup.tx_gateway) / 100) +
                ((self.price * setup.tx_tax) / 100) + self.cost), 2)

    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'

    def __str__(self):
        return self.name



TYPE_PURCHASE = (
    ('via Cartão de Crédito', 'via Cartão de Crédito'),
    ('via Boleto Bancário', 'via Boleto Bancário'),
)


class Devolution(models.Model):
    full_name = models.CharField('Nome Completo', max_length=255)
    cell_phone = models.CharField('Telefone (Whatsapp)', max_length=20)
    number_order = models.CharField('Número do Pedido', max_length=255)
    code_tracking = models.CharField('Código de Rastreio', max_length=255)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    type_purchase = models.CharField('Tipo de Compra', max_length=255, choices=TYPE_PURCHASE)
    reason = models.CharField('Motivo da devolução', max_length=255)


    class Meta:
        verbose_name = 'Trocas e Devoluções'
        verbose_name_plural = 'Trocas e Devoluções'



    def __str__(self):
        return self.full_name
