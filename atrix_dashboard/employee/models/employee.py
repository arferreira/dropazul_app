from atrix_dashboard.person.models import Person

class Employee(Person):
    class Meta:
        verbose_name = 'Colaborador'
        verbose_name_plural = 'Colaboradores'