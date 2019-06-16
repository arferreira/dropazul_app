from django.db import models


STATUS_STORE = (
    (1, 'Ativa'),
    (2, 'Inativa'),
)




class Provider(models.Model):
    name = models.CharField('Nome', max_length=255)
    local = models.Charfield('Localização', max_length=100)
    link = models.CharField('Link da Loja', max_length=255)
    whatsapp = models.CharField('Número de Whatsapp', max_length=255)


    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Modificado em')
    status = models.BooleanField(verbose_name='Situação', default=True, choices=STATUS_STORE)


    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'