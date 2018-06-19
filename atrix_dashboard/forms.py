from django.forms import ModelForm

from atrix_dashboard.models import (Customer, )


# Form para criação de clientes
class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['kind', 'name_social_name', 'cpf', 'rg',
                  'born_date', 'email', 'phone_number', 'name_fantasy',
                  'cnpj', 'responsible', 'zipcode', 'city', 'province',
                  'address', 'address_number', 'neighborhood', 'aditional_information']