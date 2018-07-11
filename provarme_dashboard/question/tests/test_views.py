from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory, Client
from django.urls import reverse_lazy


from model_mommy import mommy

from backend.question.views import QuestionListView, CategoryListView, CategoryCreateView
from backend.question.models import Question, Category
from backend.question.forms import CategoryForm



# Class responsável pelos testes na view question list
class QuestionListViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.url = reverse_lazy('question_list')
        self.user = User.objects.create_user(
            username='admin', email='admin@admin.com',
            password='123455678'
        )
        self.client = Client()
        self.questions = mommy.make(Question, _quantity=5)

    def tearDown(self):
        Question.objects.all().delete()

    def test_view_ok(self):
        request = self.factory.get(self.url)
        request.user = self.user
        response = QuestionListView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_context(self):
        request = self.factory.get(self.url)
        request.user = self.user
        response = QuestionListView.as_view()(request)
        self.assertTrue('questions' in response.context_data)
        question_list = response.context_data['questions']
        self.assertEqual(question_list.count(), 5)

# Class responsável pelos testes na view category list
class CategoryListViewTestCase(TestCase):

    def setUp(self):
        self.factory = RequestFactory()
        self.url = reverse_lazy('category_list')
        self.user = User.objects.create_user(
            username='admin', email='admin@admin.com',
            password='123455678'
        )
        self.client = Client()
        self.categories = mommy.make(Category, _quantity=5)

    def tearDown(self):
        Category.objects.all().delete()

    def test_view_ok(self):
        request = self.factory.get(self.url)
        request.user = self.user
        response = CategoryListView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_context(self):
        request = self.factory.get(self.url)
        request.user = self.user
        response = CategoryListView.as_view()(request)
        self.assertTrue('categories' in response.context_data)
        category_list = response.context_data['categories']
        self.assertEqual(category_list.count(), 5)

# Class responsável pelos testes na view de criação de categoria
class CategoryCreateViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.url = reverse_lazy('category_add')
        self.user = User.objects.create_user(
            username='admin', email='admin@admin.com',
            password='123455678'
        )

    def tearDown(self):
        pass

    def test_view_ok(self):
        request = self.factory.get(self.url)
        request.user = self.user
        response = CategoryCreateView.as_view()(request)
        self.assertEqual(response.status_code, 200)

    def test_category_form_valid(self):
        category = Category.objects.last()
        form = CategoryForm(
            data={'description': 'CPA 20',
                  'parent': category}
        )
        self.assertTrue(form.is_valid())

    def test_category_form_invalid(self):
        form = CategoryForm(data={'description': 23456,
                                  'parent': 'qualquercategoria'})
        self.assertFalse(form.is_valid())
