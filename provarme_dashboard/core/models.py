from django.db import models
from provarme_dashboard.core.manager import Manager as CustomManager


class AbstractBaseModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Modificado em')
    deleted_at = models.DateTimeField(verbose_name='Excluido em', null=True, blank=True)

    objects = CustomManager()
    objects_all = models.Manager()

    class Meta:
        abstract = True

    def delete(self):
        self.deleted_at = timezone.now()
        self.save()
        post_soft_delete.send(sender=type(self), instance=self, using=self._state.db)
