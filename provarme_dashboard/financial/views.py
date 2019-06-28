import json

from datetime import datetime, timedelta
from tenant_schemas.utils import schema_exists, schema_context, connection

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.messages.views import SuccessMessageMixin
from django.core.paginator import Paginator, InvalidPage

from provarme_dashboard.financial.forms import ExpenseForm
from provarme_dashboard.financial.models import Category, Account, Expense


# Listagem de categorias de cada tenant
class CategoryListView(LoginRequiredMixin, ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'provarme_dashboard/financial/category_list.html'


# Criando uma nova categoria
class CategoryCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Category
    fields = '__all__'
    template_name = 'provarme_dashboard/financial/category_form.html'
    success_url = reverse_lazy('dashboard:categories')
    success_message = "Categoria %(description)s foi criada com sucesso!"


# Editando uma categoria
class CategoryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Category
    fields = '__all__'
    template_name = 'provarme_dashboard/financial/category_form.html'
    success_url = reverse_lazy('dashboard:categories')
    success_message = "Categoria %(description)s foi atualizada com sucesso!"


# Listagem de contas de cada tenant
class AccountListView(LoginRequiredMixin, ListView):
    model = Account
    context_object_name = 'accounts'
    template_name = 'provarme_dashboard/financial/account_list.html'


# Criando uma nova conta
class AccountCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Account
    fields = '__all__'
    template_name = 'provarme_dashboard/financial/account_form.html'
    success_url = reverse_lazy('dashboard:accounts')
    success_message = "Conta %(name)s foi criada com sucesso!"


# Editando uma conta
class AccountUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Account
    fields = '__all__'
    template_name = 'provarme_dashboard/financial/account_form.html'
    success_url = reverse_lazy('dashboard:accounts')
    success_message = "Conta %(name)s foi atualizada com sucesso!"


######################## Expense Input ########################

class ExpenseInputListView(LoginRequiredMixin, ListView):

    model = Expense
    queryset = Expense.objects.filter(category__type_categories__in=[Category.INPUT, Category.ALL])
    context_object_name = 'expenses'
    template_name = 'provarme_dashboard/financial/expense_list.html'

    def get_context_data(self):
        context = super(ExpenseInputListView, self).get_context_data()
        context['create_url'] = reverse_lazy('dashboard:new_expense_input')
        context['update_input'] = True
        context['title'] = 'Receitas'

        return context


class ExpenseInputCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    model = Expense
    form_class = ExpenseForm
    template_name = 'provarme_dashboard/financial/expense_form.html'
    success_url = reverse_lazy('dashboard:expenses_input')
    success_message = "Receita %(name)s foi criada com sucesso!"

    def get_context_data(self, *args, **kwargs):
        context = super(ExpenseInputCreateView, self).get_context_data(*args, **kwargs)
        context['success_url'] = self.success_url
        context['title'] = 'Receita'

        return context

    def get_form(self):
        if self.request.method == 'POST':
            return self.form_class(category_type=Category.INPUT, data=self.request.POST)
        return self.form_class(category_type=Category.INPUT)


class ExpenseInputUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Expense
    form_class = ExpenseForm
    template_name = 'provarme_dashboard/financial/expense_form.html'
    success_url = reverse_lazy('dashboard:expenses_input')
    success_message = "Receita %(name)s foi atualizada com sucesso!"

    def get_context_data(self, *args, **kwargs):
        context = super(ExpenseInputUpdateView, self).get_context_data(*args, **kwargs)
        context['success_url'] = self.success_url
        context['title'] = 'Receita'

        return context

    def get_form(self):
        if self.request.method == 'POST':
            return self.form_class(instance=self.get_object(), category_type=Category.INPUT, data=self.request.POST)
        return self.form_class(instance=self.get_object(), category_type=Category.INPUT)


######################## Expense Exit ########################


class ExpenseExitListView(LoginRequiredMixin, ListView):

    model = Expense
    queryset = Expense.objects.filter(category__type_categories__in=[Category.EXIT, Category.ALL])
    context_object_name = 'expenses'
    template_name = 'provarme_dashboard/financial/expense_list.html'

    def get_context_data(self):
        context = super(ExpenseExitListView, self).get_context_data()
        context['create_url'] = reverse_lazy('dashboard:new_expense_exit')
        context['update_input'] = False
        context['title'] = 'Despesas'

        return context


class ExpenseExitCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    model = Expense
    form_class = ExpenseForm
    template_name = 'provarme_dashboard/financial/expense_form.html'
    success_url = reverse_lazy('dashboard:expenses_exit')
    success_message = "Despesa %(name)s foi criada com sucesso!"

    def get_context_data(self, *args, **kwargs):
        context = super(ExpenseExitCreateView, self).get_context_data(*args, **kwargs)
        context['success_url'] = self.success_url
        context['title'] = 'Despesa'

        return context

    def get_form(self):
        if self.request.method == 'POST':
            return ExpenseForm(category_type=Category.EXIT, data=self.request.POST)
        return ExpenseForm(category_type=Category.EXIT)


class ExpenseExitUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Expense
    form_class = ExpenseForm
    template_name = 'provarme_dashboard/financial/expense_form.html'
    success_url = reverse_lazy('dashboard:expenses_exit')
    success_message = "Despesa %(name)s foi atualizada com sucesso!"

    def get_context_data(self, *args, **kwargs):
        context = super(ExpenseExitUpdateView, self).get_context_data(*args, **kwargs)
        context['success_url'] = self.success_url
        context['title'] = 'Saída'

        return context

    def get_form(self):
        if self.request.method == 'POST':
            return ExpenseForm(instance=self.get_object(), category_type=Category.EXIT, data=self.request.POST)
        return ExpenseForm(instance=self.get_object(), category_type=Category.EXIT)
