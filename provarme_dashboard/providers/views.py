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



from provarme_dashboard.providers.models import Provider




# Listagem de fornecedores de cada tenant
class ProviderListView(LoginRequiredMixin, ListView):
    model = Provider
    context_object_name = 'providers'
    template_name = 'provarme_dashboard/providers/provider_list.html'


# Criando um fornecedor
class ProviderCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Provider
    fields = '__all__'
    template_name = 'provarme_dashboard/providers/provider_form.html'
    success_url = reverse_lazy('dashboard:providers')
    success_message = "Fornecedor foi criado com sucesso!"


# Editando um fornecedor
class ProviderUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Provider
    fields = '__all__'
    template_name = 'provarme_dashboard/providers/provider_form.html'
    success_url = reverse_lazy('dashboard:providers')
    success_message = "Fornecedor foi atualizado com sucesso!"






