from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal





class Category(models.Model):
    description = models.CharField(max_length=32)

    class Meta:
        verbose_name = "Categoria"
        permissions = (
            ("view_category", "Can view category"),
        )

    def __unicode__(self):
        s = u'%s' % (self.description)
        return s

    def __str__(self):
        s = u'%s' % (self.description)
        return s



class Brand(models.Model):
    description = models.CharField(max_length=32)

    class Meta:
        verbose_name = "Marca"
        permissions = (
            ("view_marca", "Can view brand"),
        )

    def __unicode__(self):
        s = u'%s' % (self.description)
        return s

    def __str__(self):
        s = u'%s' % (self.description)
        return s



class Unity(models.Model):
    initial_unity = models.CharField(max_length=3)
    description = models.CharField(max_length=16)

    class Meta:
        verbose_name = "Unidade"
        permissions = (
            ("view_unidade", "Can view unity"),
        )

    def __unicode__(self):
        s = u'(%s) %s' % (self.initial_unity, self.description)
        return s

    def __str__(self):
        s = u'(%s) %s' % (self.initial_unity, self.description)
        return s




class Product(models.Model):
    # Dados gerais
    code = models.CharField(max_length=15)
    barcode = models.CharField(
        max_length=16, null=True, blank=True)  # GTIN/EAN
    description = models.CharField(max_length=255)
    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.PROTECT)
    brand = models.ForeignKey(
        Brand, null=True, blank=True, on_delete=models.PROTECT)
    unity = models.ForeignKey(
        Unity, null=True, blank=True, on_delete=models.PROTECT)
    cost = models.DecimalField(max_digits=16, decimal_places=2, validators=[
                                MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))
    sale = models.DecimalField(max_digits=16, decimal_places=2, validators=[
                                MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))
    additional_information = models.CharField(max_length=255, null=True, blank=True)


    # Estoque
    stock_min = models.DecimalField(max_digits=16, decimal_places=2, validators=[
                                         MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))
    stock_currency = models.DecimalField(max_digits=16, decimal_places=2, validators=[
                                        MinValueValidator(Decimal('0.00'))], default=Decimal('0.00'))
    control_stock = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Produto"
        permissions = (
            ("view_produto", "Can view product"),
        )

    @property
    def format_unity(self):
        if self.unity:
            return self.unity.initial_unity
        else:
            return ''

    def get_initials_unity(self):
        if self.unity:
            return self.unity.initial_unity
        else:
            return ''

    def __unicode__(self):
        s = u'%s' % (self.description)
        return s

    def __str__(self):
        s = u'%s' % (self.description)
        return s