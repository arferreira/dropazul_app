from django.urls import path, include

from atrix_dashboard.views import (IndexView, CustomerListView, CustomerCreateView,
                                   CustomerUpdateView, customer_delete, ProviderListView,
                                   ProviderCreateView, ProviderUpdateView, provider_delete)

app_name="atrix_dashboard"

urlpatterns = [
    # root route
    path('', IndexView.as_view(), name='index'),
    # Clientes
    path('clientes/', CustomerListView.as_view(), name='customers'),
    path('cliente/novo', CustomerCreateView.as_view(), name='new_customer'),
    path('cliente/editar/<int:pk>', CustomerUpdateView.as_view(), name='update_customer'),
    path('cliente/excluir/<int:customer_id>', customer_delete, name='delete_customer'),
    # Fornecedores
    path('fornecedores/', ProviderListView.as_view(), name='providers'),
    path('fornecedor/novo', ProviderCreateView.as_view(), name='new_provider'),
    path('fornecedor/editar/<int:pk>', ProviderUpdateView.as_view(), name='update_provider'),
    path('fornecedor/excluir/<int:provider_id>', provider_delete, name='delete_provider'),

]