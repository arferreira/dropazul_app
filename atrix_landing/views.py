# responses django
from django.shortcuts import render, HttpResponse

# CBVs Django
from django.views.generic.base import TemplateView


class LandingPageView(TemplateView):
    template_name = 'atrix_landing/index.html'






