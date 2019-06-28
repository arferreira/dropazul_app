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

# python
from datetime import datetime, timedelta

import json

from tenant_schemas.utils import schema_exists, schema_context, connection

from provarme_dashboard.financial.models import (Category, Account, Expense)

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


# Listagem de contas a pagar de cada tenant
class ExpenseListView(LoginRequiredMixin, ListView):
    model = Expense
    context_object_name = 'expenses'
    template_name = 'provarme_dashboard/financial/expense_list.html'


# Criando uma nova contas a pagar
class ExpenseCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Expense
    fields = '__all__'
    template_name = 'provarme_dashboard/financial/expense_form.html'
    success_url = reverse_lazy('dashboard:expenses')
    success_message = "Despesa %(name)s foi criada com sucesso!"


# Editando uma contas a pagar
class ExpenseUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Expense
    fields = '__all__'
    template_name = 'provarme_dashboard/financial/expense_form.html'
    success_url = reverse_lazy('dashboard:expenses')
    success_message = "Despesa %(name)s foi atualizada com sucesso!"