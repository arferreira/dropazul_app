from django.db import models

from provarme_dashboard.core.models import AbstractBaseModel


class Traffic(AbstractBaseModel):

    product = models.ForeignKey('provarme_dashboard.Product', verbose_name='Produto', on_delete=models.CASCADE,
                                related_name='traffic')
    event_date = models.DateField(verbose_name='Data')
    investment = models.DecimalField(verbose_name='Investimento (R$)', max_digits=10, decimal_places=2)
    order_quantity = models.PositiveIntegerField(verbose_name='Número de Pedidos')

    @property
    def sales(self):
        return self.order_quantity * self.product.price

    @property
    def profit(self):
        return self.sales - (self.product.final_cost * self.order_quantity) - self.investment

    class Meta:
        verbose_name = 'Tráfego diário'
        verbose_name_plural = 'Tráfego'
        ordering = ['-event_date']
        unique_together = (('product', 'event_date'))
