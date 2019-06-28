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



from provarme_dashboard.products.models import Product
from provarme_dashboard.setups.models import Setup



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
        'name': product.name,
        'markup': product.markup,
        'price': product.price,
        'cost_fix': cost_fix,
        'cost_marketing': cost_marketing,
        'profit': profit,
        'profit_percent': profit_percent,
    }

    return render(request, 'provarme_dashboard/products/estimate.html', {'product': context})






