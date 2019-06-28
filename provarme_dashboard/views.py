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
