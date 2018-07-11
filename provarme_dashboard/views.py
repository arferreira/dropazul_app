# responses django
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
# CBVs Django
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.contrib.messages.views import SuccessMessageMixin

from tenant_schemas.utils import schema_exists, schema_context, connection


# Importação dos modelos
from provarme_dashboard.customer.models import Customer
from provarme_dashboard.provider.models import Provider
from provarme_dashboard.employee.models import Employee
from provarme_dashboard.question.models import Category
from provarme_dashboard.question.models import Question

# Importação dos forms
from provarme_dashboard.question.forms import CategoryForm
#from provarme_dashboard.question_old.forms import QuestionForm

u"""

    Informações relativas ao Aluno

"""

# Listagem de alunos de cada tenant
class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    context_object_name = 'customers'
    template_name = 'provarme_dashboard/customers/customer_list.html'


# Criando um novo aluno
class CustomerCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Customer
    fields = '__all__'
    template_name = 'provarme_dashboard/customers/customer_form.html'
    success_url = reverse_lazy('dashboard:customers')
    success_message = "Aluno %(name_social_name)s foi inserido com sucesso!"



# Editando um aluno
class CustomerUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Customer
    fields = '__all__'
    template_name = 'provarme_dashboard/customers/customer_form.html'
    success_url = reverse_lazy('dashboard:customers')
    success_message = "Aluno %(name_social_name)s foi atualizado com sucesso!"


# Deletando um aluno
@login_required
@csrf_exempt
def customer_delete(request, customer_id):
    try:
        customer = Customer.objects.get(pk=customer_id)
    except Customer.DoesNotExist:
        raise Http404()
    if request.method == 'GET':
        customer.delete()
        messages.success(request, 'Aluno excluído com sucesso!')
        return HttpResponseRedirect(reverse('dashboard:customers'))
    else:
        raise Http404()



u"""

    Informações relativas ao Professor

"""



# Listagem de professores de cada tenant
class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    template_name = 'provarme_dashboard/employees/employee_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['employees'] = Employee.objects.all()
        return context



# Criando um novo professor
class EmployeeCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Employee
    fields = '__all__'
    template_name = 'provarme_dashboard/employees/employee_form.html'
    success_url = reverse_lazy('dashboard:employees')
    success_message = "Professor %(name_social_name)s foi inserido com sucesso!"



# Editando um professor
class EmployeeUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'provarme_dashboard/employees/employee_update_form.html'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('dashboard:employees')
    success_message = "Professor %(name_social_name)s foi atualizado com sucesso!"


# Deletando um professor
@login_required
@csrf_exempt
def employee_delete(request, employee_id):
    try:
        employee = Employee.objects.get(pk=employee_id)
    except Employee.DoesNotExist:
        raise Http404()
    if request.method == 'GET':
        employee.delete()
        messages.success(request, 'Professor excluído com sucesso!')
        return HttpResponseRedirect(reverse('dashboard:employees'))
    else:
        raise Http404()



u"""

    Informações relativas as categorias
"""

# Listagem de categorias de cada tenant
class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'provarme_dashboard/categories/category_list.html'


# Criando uma nova categoria
class CategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'provarme_dashboard/categories/category_form.html'
    success_url = reverse_lazy('dashboard:categories')
    success_message = "Categoria %(description)s foi inserida com sucesso!"



# Editando uma categoria
class CategoryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'provarme_dashboard/categories/category_form.html'
    success_url = reverse_lazy('dashboard:categories')
    success_message = "Categoria %(description)s foi atualizada com sucesso!"


# Deletando uma categoria
@login_required
@csrf_exempt
def category_delete(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
    except Category.DoesNotExist:
        raise Http404()
    if request.method == 'GET':
        category.delete()
        messages.success(request, 'Categoria excluída com sucesso!')
        return HttpResponseRedirect(reverse('dashboard:categories'))
    else:
        raise Http404()




u"""

    Informações relativas as questoes
"""

# Listagem de questões de cada tenant
class QuestionListView(LoginRequiredMixin, ListView):
    model = Question
    context_object_name = 'questions'
    template_name = 'provarme_dashboard/questions/question_list.html'


# Criando uma nova questão
class QuestionCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Question
    form_class = CategoryForm
    template_name = 'provarme_dashboard/questions/question_form.html'
    success_url = reverse_lazy('dashboard:questions')
    success_message = "Questão %(wording)s foi inserida com sucesso!"



# Editando uma questão
class QuestionUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Question
    template_name = 'provarme_dashboard/questions/question_form.html'
    success_url = reverse_lazy('dashboard:questions')
    success_message = "Questão %(wording)s foi atualizada com sucesso!"


# Deletando uma questão
@login_required
@csrf_exempt
def question_delete(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404()
    if request.method == 'GET':
        question.delete()
        messages.success(request, 'Questão excluída com sucesso!')
        return HttpResponseRedirect(reverse('dashboard:questions'))
    else:
        raise Http404()