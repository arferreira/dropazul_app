from django.db import models
from django.db.models import Max
from django.template.defaultfilters import slugify
from django.urls import reverse

from mptt.models import MPTTModel, TreeForeignKey


'''

== Model referente as categorias de questões

'''

class CategoryManager(models.Manager):
    # Manager para facilitar a busca por categorias
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(description__icontains=query) | \
            models.Q(slug__icontains=query)
        )



class Category(MPTTModel):
    description = models.CharField(
        max_length=100,
        verbose_name='Descrição'
        )
    slug = models.SlugField(verbose_name='Atalho',
                            max_length=100)
    parent = TreeForeignKey(
        'self',
        null=True,
        blank=True,
        related_name='children',
        db_index=True,
        on_delete = models.CASCADE
        )
    order = models.IntegerField(
        default=0,
        verbose_name='Sequência',
        blank=False,
        null=False
        )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em'
        )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em'
    )

    class MPTTMeta:
        order_insertion_by = ['description']

    class Meta:
        unique_together = (('parent', 'slug',))
        verbose_name_plural = 'categories'




    # manager category com o método search
    objects = CategoryManager()

    def get_name(self):
        return self.description

    def __str__(self):
        ancestors = self.get_ancestors(ascending=False, include_self=True)
        return ' => '.join(category.description
                           for category in ancestors)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.description)
        super(Category, self).save(*args, **kwargs)
