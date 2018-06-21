# responses django
from django.shortcuts import render, HttpResponse

# CBVs Django
from django.views.generic.base import TemplateView


class IndexPageView(TemplateView):
    template_name = 'provarme_site/index_site.html'