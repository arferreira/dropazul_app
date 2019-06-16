from django.db import models


from provarme_dashboard.providers.models.provider import Provider

STATUS_STORE = (
    (1, 'Ativa'),
    (2, 'Inativa'),
)




class Product(models.Model):
    name = models.CharField('Nome', max_length=255)
    slug = models.SlugField('Apelido', max_length=40)
    link = models.CharField('Link para o Produto', max_length=255)
    provider = models.ForeignKey(Provider)

    cost = models.DecimalField('Custo do Produto', max_digits=5, decimal_places=2)
    markup = models.DecimalField('Markup', max_digits=3, decimal_places=2)

    recommended_price = models.DecimalField('Preço recomendado', max_digits=5, decimal_places=2)
    price = models.DecimalField('Preço Final', max_digits=5, decimal_places=2)


    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Modificado em')
    status = models.BooleanField(verbose_name='Situação', default=True, choices=STATUS_STORE)


    class Meta:
        verbose_name = 'Produto'
        verbose_name_plural = 'Produtos'