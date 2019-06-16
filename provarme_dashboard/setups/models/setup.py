from django.db import models


STATUS_STORE = (
    (1, 'Ativa'),
    (2, 'Inativa'),
)




class Setup(models.Model):
    tx_shopify = models.DecimalField('Taxa Shopify', max_digits=3, decimal_places=2)
    tx_gateway = models.DecimalField('Taxa do Gateway', max_digits=3, decimal_places=2)
    tx_antecipation = models.DecimalField('Taxa de Antecipação', max_digits=3, decimal_places=2)
    tx_tax = models.DecimalField('Imposto', max_digits=3, decimal_places=2)
    tx_iof = models.DecimalField('IOF', max_digits=3, decimal_places=2)
    tx_cashback = models.DecimalField('Cashback', max_digits=3, decimal_places=2)


    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Modificado em')
    status = models.BooleanField(verbose_name='Situação', default=True, choices=STATUS_STORE)


    class Meta:
        verbose_name = 'Configuração'
        verbose_name = 'Configurações'