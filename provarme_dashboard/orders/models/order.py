from django.db import models

STATUS_STORE = (
    (1, 'Ativa'),
    (2, 'Inativa'),
)


class Order(models.Model):
    name = models.CharField('Nome da Loja', max_length=100)
    initials = models.CharField('Sigla da Loja', max_length=100)
    url = models.CharField('URL da Loja', max_length=100)
    client_id_mp = models.CharField('CLIENT_ID (Mercado Pago)', max_length=255)
    client_secret_mp = models.CharField('CLIENT_SECRET (Mercado Pago)', max_length=255)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Modificado em')
    status = models.BooleanField(verbose_name='Situação', default=True, choices=STATUS_STORE)


    class Meta:
        verbose_name = 'Loja'
        verbose_name = 'Lojas'

    def __str__(self):
        return self.name