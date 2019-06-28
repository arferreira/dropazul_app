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



from provarme_dashboard.store.models import Store



# Listagem de loja de cada tenant
class StoreListView(LoginRequiredMixin, ListView):
    
    model = Store
    context_object_name = 'stores'
    template_name = 'provarme_dashboard/stores/store_list.html'


# Criando uma nova loja
class StoreCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    model = Store
    fields = '__all__'
    template_name = 'provarme_dashboard/stores/store_form.html'
    success_url = reverse_lazy('dashboard:stores')
    success_message = "Loja %(name)s foi criada com sucesso!"


# Editando uma loja
class StoreUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Store
    fields = '__all__'
    template_name = 'provarme_dashboard/stores/store_form.html'
    success_url = reverse_lazy('dashboard:stores')
    success_message = "Loja %(name)s foi atualizada com sucesso!"
