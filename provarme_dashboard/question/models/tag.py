from django.db import models


class Tag(models.Model):
	"""
	Declaração do model Tag
	"""
	description = models.CharField(
		'Descrição', max_length=50
	)

	tag = models.SlugField(
		'Tag'
	)

	created_at = models.DateTimeField(
		auto_now_add=True,
		verbose_name='Criado em'
	)
	updated_at = models.DateTimeField(
		auto_now=True,
		verbose_name='Atualizado em'
	)



	def __str__(self):
		return self.description
