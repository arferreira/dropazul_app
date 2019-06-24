# responses django
import json
import requests
from django.shortcuts import render, HttpResponse

from django.views.decorators.csrf import csrf_protect


# CBVs Django
from django.views.generic.base import TemplateView


from provarme_dashboard.products.models import Devolution

from .forms import DevolutionForm

# View para landing do cliente
class IndexPageView(TemplateView):
    template_name = 'provarme_site/index_site.html'


# View para rastreamento de objetos dos correios
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






# View para trocas e devoluções (Client side)
def devolution(request):

    if request.method == 'GET':
        template = 'provarme_site/devolutions_form.html'
        form = DevolutionForm()
    elif request.method == 'POST':
        template = 'provarme_site/devolutions_success.html'
        form = DevolutionForm(request.POST)
        if form.is_valid():
            devolution = form.save(commit=False)
            devolution.save()

    return render(request, template, {'form': form})