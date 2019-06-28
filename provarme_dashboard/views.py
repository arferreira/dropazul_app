import json

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


# Importação Modelos

from provarme_dashboard.setups.models import Setup
from provarme_dashboard.providers.models import Provider
from provarme_dashboard.products.models import Product
from provarme_dashboard.traffic.models import Traffic
from provarme_dashboard.order.models import Order
from provarme_dashboard.products.models import Devolution
from provarme_dashboard.customer.models import Customer







# Listagem de pedidos de cada tenant
class OrderListView(LoginRequiredMixin, ListView):
    model = Order
    context_object_name = 'orders'
    template_name = 'provarme_dashboard/orders/order_list.html'


# Listagem de clientes de cada tenant
class CustomerListView(LoginRequiredMixin, ListView):
    model = Customer
    context_object_name = 'customers'
    template_name = 'provarme_dashboard/customers/customer_list.html'


# Listagem de setup de cada tenant
class SetupListView(LoginRequiredMixin, ListView):
    model = Setup
    context_object_name = 'setups'
    template_name = 'provarme_dashboard/setups/setup_list.html'


# Criando um setup
class SetupCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Setup
    fields = '__all__'
    template_name = 'provarme_dashboard/setups/setup_form.html'
    success_url = reverse_lazy('dashboard:setups')
    success_message = "Configuração foi criada com sucesso!"


# Editando um setup
class SetupUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Setup
    fields = '__all__'
    template_name = 'provarme_dashboard/setups/setup_form.html'
    success_url = reverse_lazy('dashboard:setups')
    success_message = "Configuração foi atualizada com sucesso!"


# Listagem de fornecedores de cada tenant
class ProviderListView(LoginRequiredMixin, ListView):
    model = Provider
    context_object_name = 'providers'
    template_name = 'provarme_dashboard/providers/provider_list.html'


# Criando um setup
class ProviderCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Provider
    fields = '__all__'
    template_name = 'provarme_dashboard/providers/provider_form.html'
    success_url = reverse_lazy('dashboard:providers')
    success_message = "Fornecedor foi criado com sucesso!"


# Editando um setup
class ProviderUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Provider
    fields = '__all__'
    template_name = 'provarme_dashboard/providers/provider_form.html'
    success_url = reverse_lazy('dashboard:providers')
    success_message = "Fornecedor foi atualizado com sucesso!"


# Listagem de produtos de cada tenant
class ProductListView(LoginRequiredMixin, ListView):
    model = Product
    context_object_name = 'products'
    template_name = 'provarme_dashboard/products/product_list.html'


# Criando um product
class ProductCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Product
    fields = '__all__'
    template_name = 'provarme_dashboard/products/product_form.html'
    success_url = reverse_lazy('dashboard:products')
    success_message = "Produto foi criado com sucesso!"


# Editando um product
class ProductUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Product
    fields = '__all__'
    template_name = 'provarme_dashboard/products/product_form.html'
    success_url = reverse_lazy('dashboard:products')
    success_message = "Produto foi atualizado com sucesso!"


# Estimativa de lucro de um produto
def product_estimate(request, pk):
    setup = Setup.objects.all().first()
    product = Product.objects.get(pk=pk)

    cost_fix = product.final_cost
    
    cost_marketing = round(product.price * product.marketing / 100, 2)
    profit = round(product.price - cost_fix - cost_marketing, 2)
    profit_percent = round(profit / product.price * 100, 2)

    context = {
        'markup': product.markup,
        'price': product.price,
        'cost_fix': cost_fix,
        'cost_marketing': cost_marketing,
        'profit': profit,
        'profit_percent': profit_percent,
    }

    return render(request, 'provarme_dashboard/products/estimate.html', {'product': context})


# Listagem de trocas e devoluções de cada tenant
class DevolutionsListView(LoginRequiredMixin, ListView):
    model = Devolution
    context_object_name = 'devolutions'
    template_name = 'provarme_dashboard/devolutions/devolution_list.html'


# Listando o tráfego diário
def traffic_list(request):
    traffic = Traffic.objects.all()

    context = {
        'traffic': traffic,
    }

    return render(request, 'provarme_dashboard/traffic/traffic_list.html', context)


# class CashFlowListView(LoginRequiredMixin, ListView):
#
#     model = CashFlow
#     template_name = 'provarme_dashboard/cash_flow/cash_flow_list.html'

# View para gerenciar suporte
def support_index_view(request):
    page = request.GET.get('page')
    paginator = Paginator(Order.objects.filter(
        financial_status='pending', updated_at__gte=datetime.now()-timedelta(days=7)), 2)
    total = paginator.count

    try:
        orders_last_7_days = paginator.page(page)
    except InvalidPage:
        orders_last_7_days = paginator.page(1)

    context = {
        'orders': orders_last_7_days,
        'total': total,
    }
    return render(request, 'provarme_dashboard/support/support_index.html', context)
