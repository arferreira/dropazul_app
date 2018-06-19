from django.urls import path, include

from atrix_dashboard.views import (IndexView, CustomerListView, CustomerCreateView,
                                   CustomerUpdateView, customer_delete)

app_name="atrix_dashboard"

urlpatterns = [
    # root route
    path('', IndexView.as_view(), name='index'),
    # Clientes
    path('clientes/', CustomerListView.as_view(), name='customers'),
    path('cliente/novo', CustomerCreateView.as_view(), name='new_customer'),
    path('cliente/editar/<int:pk>', CustomerUpdateView.as_view(), name='update_customer'),
    path('cliente/excluir/<int:customer_id>', customer_delete, name='delete_customer'),

]