from django.db import models


# model para gestão de categorias
class Category(models.Model):
    TYPES = (
        ('E', 'Entrada'),
        ('S', 'Saída'),
        ('T', 'Todos')
    )
    description = models.CharField('Descrição', max_length=40, unique=True)
    is_active = models.BooleanField('ativa', default=True)
    type_categories = models.CharField(
        'tipo', choices=TYPES, default='S', max_length=1)

    class Meta:
        ordering = ['description']

    def __unicode__(self):
        self.description

    def save(self, *args, **kwargs):
        self.description = self.description.upper()
        super(Category, self).save(*args, **kwargs)

    @property
    def get_absolute_url(self):
        return reverse('category_update', args=[str(self.id)])





# model para gestão de contas
class Account(models.Model):
    name = models.CharField("Nome", max_length=250, unique=True)
    balance = models.DecimalField('Saldo', max_digits=10, decimal_places=2, default=0)
    balance_date = models.DateTimeField('Data', null=True, blank=True)

    created_at = models.DateTimeField("Criado em",  auto_now_add=True)
    updated_at = models.DateTimeField("Atualizado em",  auto_now=True)

    class Meta:
        ordering = ['name']


    def __str__(self):
        return self.name
