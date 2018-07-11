from django.db import models
from django.contrib.auth.models import User

from mptt.models import TreeManyToManyField

from .alternative import Alternative
from .category import Category
from .tag import Tag


class QuestionManager(models.Manager):
    # custom manager para busca de questões por enunciado
    def search(self, query):
        return self.get_queryset().filter(
            models.Q(wording__icontains=query) |
            models.Q(hint__icontains=query)
        )


class Question(models.Model):
    """
    Classe principal de questões
    """
    exam = models.ManyToManyField(
        'exam.Exam',
        verbose_name='Simulado',
        related_name='questions'
    )


    wording = models.TextField(
        'Enunciado'
    )
    categories = TreeManyToManyField(
        Category,
        verbose_name='Categoria'
    )

    tags = models.ManyToManyField(
        Tag, verbose_name='Tags'
    )

    hint = models.TextField(
        'Dica',
        blank=True
    )

    comment = models.TextField(
        'Comentário',
        blank=True
    )

    active = models.BooleanField('Avita', default=True)

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Criado em'
        )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Atualizado em'
    )

    objects = QuestionManager()

    def __str__(self):
        import html2text
        return html2text.html2text(self.wording)


class UserAnswer(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Usuário',
        on_delete=models.PROTECT
    )
    exam_result = models.ForeignKey(
        'exam.ExamResult',
        verbose_name='Exame',
        on_delete=models.PROTECT
    )
    question = models.ForeignKey(
        Question,
        verbose_name='Questão',
        on_delete=models.PROTECT
    )
    alternative = models.ForeignKey(
        Alternative,
        verbose_name='Resposta',
        on_delete=models.PROTECT
    )
    time = models.PositiveSmallIntegerField(
        default=0,
        blank=True,
        null=True
    )
