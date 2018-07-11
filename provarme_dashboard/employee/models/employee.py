from provarme_dashboard.person.models import Person

class Employee(Person):
    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'