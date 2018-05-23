# responses django
from django.shortcuts import render, HttpResponse

# CBVs Django
from django.views.generic.base import TemplateView


class IndexPageView(TemplateView):
    template_name = 'atrix_site/index_site.html'