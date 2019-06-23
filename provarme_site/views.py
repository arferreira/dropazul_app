# responses django
import json
import requests
from django.shortcuts import render, HttpResponse
from correios import Correios
from django.views.decorators.csrf import csrf_protect


# CBVs Django
from django.views.generic.base import TemplateView


class IndexPageView(TemplateView):
    template_name = 'provarme_site/index_site.html'



def tracking_order(request):
    if request.method == "GET":
        template = "provarme_site/tracking_order.html"
        eventos = {}
    elif request.method == "POST":
        template = "provarme_site/tracking_result.html"
        code = request.POST.get('code', None)
        url = "https://api.postmon.com.br/v1/rastreio/ect/{}".format(code)
        data = requests.get(url).json()

        eventos = data['historico']
    return render(request, template, context={'eventos': eventos})

