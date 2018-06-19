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


# Dashboard (Painel do cliente)
from atrix_dashboard.models import Customer
# Form Customer
from atrix_dashboard.forms import CustomerForm


class IndexView(LoginRequiredMixin, TemplateView):
    login_url = '/tenant/login/'
    template_name = 'atrix_dashboard/index_dashboard.html'


# Listagem de clientes de cada tenant
class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    context_object_name = 'customers'
    template_name = 'atrix_dashboard/customers/customer_list.html'


# Criando um novo cliente
class CustomerCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Customer
    fields = '__all__'
    template_name = 'atrix_dashboard/customers/customer_form.html'
    success_url = reverse_lazy('dashboard:customers')
    success_message = "Cliente %(name_social_name)s foi inserido com sucesso!"



# Editando um cliente
class CustomerUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Customer
    fields = '__all__'
    template_name = 'atrix_dashboard/customers/customer_update_form.html'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('dashboard:customers')
    success_message = "Cliente %(name_social_name)s foi atualizado com sucesso!"


# Deletando um cliente
@login_required
@csrf_exempt
def customer_delete(request, customer_id):
    try:
        customer = Customer.objects.get(pk=customer_id)
    except Customer.DoesNotExist:
        raise Http404()
    if request.method == 'GET':
        customer.delete()
        messages.success(request, 'Cliente excluído com sucesso!')
        return HttpResponseRedirect(reverse('dashboard:customers'))
    else:
        raise Http404()












