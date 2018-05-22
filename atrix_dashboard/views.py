# responses django
from django.shortcuts import render, HttpResponse

# CBVs Django
from django.views.generic.base import TemplateView


class IndexView(TemplateView):
    template_name = 'atrix_dashboard/index_dashboard.html'