from django.db import models


class Provider(models.Model):

    STATUS_STORE = (
        (True, 'Ativo'),
        (False, 'Inativo'),
    )

    name = models.CharField('Nome', max_length=255)
    local = models.CharField('Localização', max_length=100)
    link = models.CharField('Link da Loja', max_length=255)
    whatsapp = models.CharField('Número de Whatsapp', max_length=255)
    status = models.BooleanField(verbose_name='Situação', default=True, choices=STATUS_STORE)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Modificado em')

    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'

    def __str__(self):
        return self.name
