from django.test import TestCase
from django.template.defaultfilters import slugify
from model_mommy import mommy


from backend.question.models import (
    Question,
    Tag,
    Category,
    CategoryManager,
    )

# classe para testes do model Question
class QuestionTestCase(TestCase):

    def setUp(self):
        category = Category.objects.create(description='CPA 10')
        category.save()
        category = Category.objects.last()
        self.questions_cpa10 = mommy.make(
            Question,
            wording = 'cpa 10',
            category_id = category.pk,
            hint = 'atividades previstas na CPA0-10 e CPA-10',
            _quantity=5
        )

        self.questions_cpa20 = mommy.make(
            Question,
            wording = 'cpa 20',
            category = category,
            hint = 'atividades previstas na CPA0-10 e CPA-20',
            _quantity=15
        )

    def tearDown(self):
        Question.objects.all().delete()


    def test_objects_created(self):
        """
            Verificando a persistencia dos objetos criados
        """
        self.assertEqual(Question.objects.count(), 20)


    def test_question_search(self):
        """
            Testando o custom manager de question através do método search
        """
        search_cpa20 = Question.objects.search('cpa 20')
        self.assertEqual(len(search_cpa20), 15)
        search_cpa10 = Question.objects.search('cpa 10')
        self.assertEqual(len(search_cpa10), 5)



# Classe para testes do model Tag
class TagTestCase(TestCase):

    def setUp(self):
        self.tags = mommy.make(
            Tag,
            description = 'cap-20',
            _quantity=3
        )

    def tearDown(self):
        Tag.objects.all().delete()

    def test_objects_created(self):
        """
            Verifica se os objetos que foram criados persistiram com segurança
        """
        self.assertEqual(Tag.objects.count(), 3)


# Classe para testes do model Category
class CategoryTestCase(TestCase):

    def setUp(self):
        top = Category(description='Top category', slug=slugify('Top category'))
        top.save()
        level1_first = Category(description='Level1 first', slug=slugify('Level1 first'), parent=top)
        level1_first.save()
        level1_second = Category(description='Level1 second', slug=slugify('Level1 second'),  parent=top)
        level1_second.save()
        level2_first = Category(description='Level2 first', slug=slugify('Level2 first'), parent=level1_first)
        level2_first.save()
        level2_first_sub = Category(description='Level2 first sub', slug=slugify('Level2 first sub'), parent=level2_first)
        level2_first_sub.save()
        level2_second = Category(description='Level2 second', slug=slugify('Level2 second'), parent=level1_first)
        level2_second.save()
        top_two = Category(description='Top category two', slug=slugify('Top category two'))
        top_two.save()
        level1_two_first = Category(description='Level1 two first', slug=slugify('Level1 two first'), parent=top_two)
        level1_two_first.save()
        level1_two_second = Category(description='Level1 two second', slug=slugify('Level1 two second'), parent=top_two)
        level1_two_second.save()
        level1_two_second_sub = Category(description='Level1 two second sub', slug=slugify('Level1 two second sub'), parent=level1_two_second)
        level1_two_second_sub.save()


    def tearDown(self):
        Category.objects.all().delete()

    def test_category_str(self):
        self.assertEqual(str(Category.objects.get(slug='level1-first')), 'Top category -> Level1 first')

    def test_objects_created(self):
        self.assertEqual(Category.objects.count(), 10)


    def test_category_search(self):
        """
            Testa a a busca através do custom manager search criado
        """
        search = Category.objects.search('Top category')
        self.assertEqual(len(search), 2)
