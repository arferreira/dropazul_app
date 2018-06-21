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
from atrix_dashboard.customer.models import Customer
from atrix_dashboard.provider.models import Provider
from atrix_dashboard.employee.models import Employee




u"""

    Informações relativas ao Cliente

"""

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


u"""

    Informações relativas ao Fornecedor

"""



# Listagem de fornecedores de cada tenant
class ProviderListView(LoginRequiredMixin, ListView):
    model = Provider
    context_object_name = 'providers'
    template_name = 'atrix_dashboard/providers/provider_list.html'


# Criando um novo fornecedor
class ProviderCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Provider
    fields = '__all__'
    template_name = 'atrix_dashboard/providers/provider_form.html'
    success_url = reverse_lazy('dashboard:providers')
    success_message = "Fornecedor %(name_social_name)s foi inserido com sucesso!"



# Editando um fornecedor
class ProviderUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Provider
    fields = '__all__'
    template_name = 'atrix_dashboard/providers/provider_update_form.html'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('dashboard:providers')
    success_message = "Fornecedor %(name_social_name)s foi atualizado com sucesso!"


# Deletando um fornecedor
@login_required
@csrf_exempt
def provider_delete(request, provider_id):
    try:
        provider = Provider.objects.get(pk=provider_id)
    except Provider.DoesNotExist:
        raise Http404()
    if request.method == 'GET':
        provider.delete()
        messages.success(request, 'Fornecedor excluído com sucesso!')
        return HttpResponseRedirect(reverse('dashboard:providers'))
    else:
        raise Http404()



u"""

    Informações relativas ao Colaborador

"""



# Listagem de funcionarios de cada tenant
class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee
    context_object_name = 'employees'
    template_name = 'atrix_dashboard/employees/employee_list.html'


# Criando um novo funcionario
class EmployeeCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Employee
    fields = '__all__'
    template_name = 'atrix_dashboard/employees/employee_form.html'
    success_url = reverse_lazy('dashboard:employees')
    success_message = "Colaborador %(name_social_name)s foi inserido com sucesso!"



# Editando um funcionario
class EmployeeUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Employee
    fields = '__all__'
    template_name = 'atrix_dashboard/employees/employee_update_form.html'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('dashboard:employees')
    success_message = "Colaborador %(name_social_name)s foi atualizado com sucesso!"


# Deletando um funcionario
@login_required
@csrf_exempt
def employee_delete(request, employee_id):
    try:
        employee = Employee.objects.get(pk=employee_id)
    except Employee.DoesNotExist:
        raise Http404()
    if request.method == 'GET':
        employee.delete()
        messages.success(request, 'Colaborador excluído com sucesso!')
        return HttpResponseRedirect(reverse('dashboard:employees'))
    else:
        raise Http404()

