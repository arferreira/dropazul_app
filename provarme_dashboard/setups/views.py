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


from provarme_dashboard.setups.models import Setup


class SetupListView(LoginRequiredMixin, ListView):

    model = Setup
    context_object_name = 'setups'
    template_name = 'provarme_dashboard/setups/setup_list.html'


class SetupCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    model = Setup
    fields = '__all__'
    template_name = 'provarme_dashboard/setups/setup_form.html'
    success_url = reverse_lazy('dashboard:setups')
    success_message = "Configuração foi criada com sucesso!"

    def get(self, request):
        setup = self.model.objects.first()
        if setup:
            return HttpResponseRedirect(reverse_lazy('dashboard:update_setup', args=[setup.pk]))

        return super(SetupCreateView, self).get(request)


class SetupUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Setup
    fields = '__all__'
    template_name = 'provarme_dashboard/setups/setup_form.html'
    success_url = reverse_lazy('dashboard:setups')
    success_message = "Configuração foi atualizada com sucesso!"
