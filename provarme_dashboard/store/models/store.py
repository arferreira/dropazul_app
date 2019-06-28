from django.db import models


class Store(models.Model):

    STATUS = (
        (True, 'Ativo'),
        (False, 'Inativo'),
    )

    name = models.CharField('Nome da Loja', max_length=100)
    initials = models.CharField('Sigla da Loja', max_length=100)
    url = models.CharField('URL da Loja', max_length=100)
    client_id_mp = models.CharField('CLIENT_ID (Mercado Pago)', max_length=255)
    client_secret_mp = models.CharField('CLIENT_SECRET (Mercado Pago)', max_length=255)
    status = models.BooleanField(verbose_name='Situação', default=True, choices=STATUS)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Modificado em')

    class Meta:
        verbose_name = 'Loja'
        verbose_name_plural = 'Lojas'

    def __str__(self):
        return self.name
