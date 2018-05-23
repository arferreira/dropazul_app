# responses django
from django.shortcuts import render, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
# CBVs Django
from django.views.generic.base import TemplateView


class IndexView(LoginRequiredMixin, TemplateView):
    login_url = '/tenant/login/'
    template_name = 'atrix_dashboard/index_dashboard.html'