from django.db import models
from django.contrib.auth.models import User



class Alternative(models.Model):
    """
    Declaração do model Answer
    """
    text = models.TextField(
        'Alternativa'
    )

    correct = models.BooleanField(
        'Alternativa correta?', default=False
    )

    question = models.ForeignKey(
        'question.Question',
        on_delete=models.PROTECT,
        verbose_name='Questão',
        related_name='alternatives'
    )

    def __str__(self):
        return "{0}-{1}".format(self.text, self.question)
