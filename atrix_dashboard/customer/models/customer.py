from atrix_dashboard.person.models import Person


# Modelo referente a clientes
class Customer(Person):
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'