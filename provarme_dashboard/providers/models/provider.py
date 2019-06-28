from django.db import models
from provarme_dashboard.core.models import AbstractBaseModel


class Provider(AbstractBaseModel):

    STATUS_STORE = (
        (True, 'Ativo'),
        (False, 'Inativo'),
    )

    name = models.CharField('Nome', max_length=255)
    local = models.CharField('Localização', max_length=100)
    link = models.CharField('Link da Loja', max_length=255)
    whatsapp = models.CharField('Número de Whatsapp', max_length=255)
    status = models.BooleanField(verbose_name='Situação', default=True, choices=STATUS_STORE)

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.name
