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
