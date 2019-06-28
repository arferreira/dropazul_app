import re
from decimal import Decimal
from django import template

register = template.Library()


@register.filter('text_color')
def text_color(value):
    return 'success' if value else 'danger'


@register.filter('money_color')
def money_color(value):
    color = ''

    if value > Decimal('0.00'):
        color = 'success'
    elif value < Decimal('0.00'):
        color = 'danger'

    return color


@register.filter('clean_phone')
def clean_phone(value):
    return "55" + re.sub(r'[^0-9]', '', value)
