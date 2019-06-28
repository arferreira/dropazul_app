from decimal import Decimal
from datetime import datetime
from dateutil.relativedelta import relativedelta

from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

from provarme_dashboard.traffic.models import Traffic


class CashFlowListView(LoginRequiredMixin, TemplateView):

    template_name = 'provarme_dashboard/cash_flow/list.html'

    def get(self, request):
        context = {
            'object_list': [],
            'total_shopping': Decimal('0.00'),
            'total_sales': Decimal('0.00'),
            'total_traffic': Decimal('0.00'),
            'total_tax': Decimal('0.00'),
            'total_profit_real': Decimal('0.00'),
            'total_profit_percentage': Decimal('0.00'),
        }
        now = datetime.now()
        first_day = now + relativedelta(day=1)
        last_day = now + relativedelta(day=1, months=+1, days=-1)

        for index in range(first_day.day, last_day.day+1):
            date = datetime(now.year, now.month, index)
            traffic = Traffic.objects.filter(event_date=date)

            sales = sum([t.sales for t in traffic]) or Decimal('0.00')
            profit_real = sum([t.profit for t in traffic]) or Decimal('0.00')
            profit_percentage = round((profit_real * 100) / sales, 2) if profit_real and sales else Decimal('0.00')

            obj = {
                'date': date,
                'shopping': sum([t.order_quantity * t.product.final_cost for t in traffic]) or Decimal('0.00'),
                'sales': sales,
                'traffic': sum([t.investment for t in traffic]) or Decimal('0.00'),
                'tax': sum([t.product.final_cost for t in traffic]) or Decimal('0.00'),
                'profit_real': profit_real,
                'profit_percentage': profit_percentage,
            }

            context['total_shopping'] += obj['shopping']
            context['total_sales'] += obj['sales']
            context['total_traffic'] += obj['traffic']
            context['total_tax'] += obj['tax']
            context['total_profit_real'] += obj['profit_real']
            # context['total_profit_percentage'] += obj['profit_percentage']

            context['object_list'].append(obj)

        # context['total_profit_percentage'] = round((context['total_profit_percentage'] * 100) / len(context['object_list']), 2)

        return render(request, self.template_name, context)
