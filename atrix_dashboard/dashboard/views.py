from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
# CBVs Django
from django.views.generic.base import TemplateView





# Importação dos modelos
from atrix_dashboard.customer.models import Customer



u"""

    Views relativas ao Dashboard

"""


# Tela Inicial do Dashboard
class IndexView(LoginRequiredMixin, TemplateView):
    login_url = '/tenant/login/'
    template_name = 'atrix_dashboard/index_dashboard.html'
    customers = Customer.objects.all()

    def get(self, request):
        return render(request, self.template_name, {'customers': self.customers})





