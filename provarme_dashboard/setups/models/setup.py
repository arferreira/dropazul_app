from django.db import models


class Setup(models.Model):

    STATUS = (
        (True, 'Ativo'),
        (False, 'Inativo'),
    )

    tx_shopify = models.DecimalField('Taxa Shopify', max_digits=3, decimal_places=2)
    tx_gateway = models.DecimalField('Taxa do Gateway', max_digits=3, decimal_places=2)
    tx_antecipation = models.DecimalField('Taxa de Antecipação', max_digits=3, decimal_places=2)
    tx_tax = models.DecimalField('Imposto', max_digits=3, decimal_places=2)
    tx_iof = models.DecimalField('IOF', max_digits=3, decimal_places=2)
    tx_cashback = models.DecimalField('Cashback', max_digits=3, decimal_places=2)
    status = models.BooleanField(verbose_name='Situação', default=True, choices=STATUS)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Modificado em')

    class Meta:
        verbose_name = 'Configuração'
        verbose_name_plural = 'Configurações'
