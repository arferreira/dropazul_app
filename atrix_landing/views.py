# responses django
from django.shortcuts import render, HttpResponse, HttpResponseRedirect, redirect
from django.urls import reverse_lazy
from tenant_schemas.utils import connection

# CBVs Django
from django.views.generic.base import TemplateView

# atrix views
from atrix_site.views import IndexPageView


class LandingPageView(TemplateView):
    template_name = 'atrix_landing/index.html'










