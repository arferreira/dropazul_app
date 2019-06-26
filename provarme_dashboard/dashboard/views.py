from datetime import date

from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
# CBVs Django
from django.views.generic.base import TemplateView



from provarme_dashboard.order.models import Order
from provarme_dashboard.customer.models import Customer



# Importação dos modelos
#from provarme_dashboard.customer.models import Customer



u"""

    Views relativas ao Dashboard

"""


# Tela Inicial do Dashboard
@login_required
def index_view(request):
    templates_name = 'provarme_dashboard/index_dashboard.html'
    today = date.today()

    orders_today = Order.objects.filter(created_at__year=today.year, created_at__month=today.month, created_at__day=today.day)
    total_amount = 0
    total_paid = 0
    total_pending = 0
    for order in orders_today:
        total_amount += order.total_price
        if order.financial_status == 'pending':
            total_pending += order.total_price
        elif order.financial_status == 'paid':
            total_paid += order.total_price

        

    # quantidade de clientes
    customers = Customer.objects.all()
    qt_customers = customers.count()
    # total de boletos do dia
    print(orders_today)
    context = {
        'qt_customers': qt_customers,
        'total_paid': total_paid,
        'total_pending': total_pending,
        'total_amount': total_amount,
        }
    return render(request, templates_name, context)










