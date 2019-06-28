from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin

from provarme_dashboard.traffic.models import Traffic
from provarme_dashboard.traffic.forms import TrafficForm


class TrafficListView(LoginRequiredMixin, ListView):

    model = Traffic
    template_name = 'provarme_dashboard/traffic/traffic_list.html'


class TrafficCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):

    model = Traffic
    form_class = TrafficForm
    template_name = 'provarme_dashboard/traffic/traffic_form.html'
    success_url = reverse_lazy('dashboard:traffic')
    success_message = "Tráfego criado com sucesso!"


class TrafficUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):

    model = Traffic
    form_class = TrafficForm
    template_name = 'provarme_dashboard/traffic/traffic_form.html'
    success_url = reverse_lazy('dashboard:traffic')
    success_message = "Tráfego atualizado com sucesso!"
