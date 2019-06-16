from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
# CBVs Django
from django.views.generic.base import TemplateView





# Importação dos modelos
#from provarme_dashboard.customer.models import Customer



u"""

    Views relativas ao Dashboard

"""


# Tela Inicial do Dashboard
class IndexView(LoginRequiredMixin, TemplateView):
    login_url = '/tenant/login/'
    template_name = 'provarme_dashboard/index_dashboard.html'
    customers = 2

    def get(self, request):
        return render(request, self.template_name, {'customers': self.customers})





