# responses django
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.urls import reverse_lazy
from tenant_schemas.utils import connection

# CBVs Django
from django.views.generic.base import TemplateView

# atrix views
from provarme_site.views import IndexPageView


class LandingPageView(TemplateView):
    template_name = 'provarme_landing/index.html'










