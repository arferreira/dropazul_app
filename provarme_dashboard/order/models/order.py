from django.db import models
from django.contrib.postgres.fields import JSONField


class OrderManager(models.Manager):

    def get_or_create_order(self, customer, body):
        obj, _ = Order.objects.get_or_create(customer=customer, shopify_id=body['id'])
        obj.total_price = body['total_price']
        obj.financial_status = body['financial_status']
        obj.order_number = body['order_number']
        obj.created_at = body['created_at']
        obj.updated_at = body['updated_at']
        obj.body = body

        obj.save()

        return obj


class Order(models.Model):

    customer = models.ForeignKey('provarme_dashboard.Customer', related_name='orders', on_delete=models.CASCADE)
    shopify_id = models.CharField('ID Shopify', max_length=50)

    total_price = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    financial_status = models.CharField(max_length=255, null=True, blank=True)
    order_number = models.CharField(max_length=255, null=True, blank=True)

    body = JSONField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Modificado em')

    objects = OrderManager()

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'

    def __str__(self):
        return self.name
