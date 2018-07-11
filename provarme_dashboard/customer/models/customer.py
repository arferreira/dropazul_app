from provarme_dashboard.person.models import Person


# Modelo referente a alunos
class Customer(Person):
    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'