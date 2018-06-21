from provarme_dashboard.person.models import *

# Modelo referente a Fornecedor
class Provider(Person):
    class Meta:
        verbose_name = 'Fornecedor'
        verbose_name_plural = 'Fornecedores'