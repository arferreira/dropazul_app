from django.conf.urls import url
from django.urls import path, include

# views Dashboard
from provarme_dashboard.dashboard.views import index_view as dashboard_index

from provarme_dashboard.views import *
from provarme_dashboard.financial.views import *
from provarme_dashboard.store.views import StoreListView, StoreCreateView, StoreUpdateView
from provarme_dashboard.setups.views import SetupListView, SetupCreateView, SetupUpdateView
from provarme_dashboard.providers.views import ProviderListView, ProviderCreateView, ProviderUpdateView
from provarme_dashboard.products.views import ProductListView, ProductCreateView, ProductUpdateView, product_estimate
from provarme_dashboard.traffic.views import TrafficListView, TrafficCreateView, TrafficUpdateView
from provarme_dashboard.cash_flow.views import CashFlowListView


app_name = 'provarme_dashboard'

urlpatterns = [
    # Rota principal do dashboard
    path('visao-geral/', dashboard_index, name='index'),

    # Store
    path('loja/', StoreListView.as_view(), name='stores'),
    path('loja/nova', StoreCreateView.as_view(), name='new_store'),
    path('loja/editar/<int:pk>', StoreUpdateView.as_view(), name='update_store'),

    # Categories
    path('categorias/', CategoryListView.as_view(), name='categories'),
    path('categoria/nova', CategoryCreateView.as_view(), name='new_category'),
    path('categoria/editar/<int:pk>', CategoryUpdateView.as_view(), name='update_category'),

    # Contas
    path('contas/', AccountListView.as_view(), name='accounts'),
    path('conta/nova', AccountCreateView.as_view(), name='new_account'),
    path('conta/editar/<int:pk>', AccountUpdateView.as_view(), name='update_account'),

    # Contas a Pagar
    path('contas-a-pagar/', ExpenseListView.as_view(), name='expenses'),
    path('contas-a-pagar/nova', ExpenseCreateView.as_view(), name='new_expense'),
    path('contas-a-pagar/editar/<int:pk>', ExpenseUpdateView.as_view(), name='update_expense'),
    path('fluxo-de-caixa/', CashFlowListView.as_view(), name='cash-flow'),

    # Setups
    path('setup/', SetupListView.as_view(), name='setups'),
    path('setup/novo', SetupCreateView.as_view(), name='new_setup'),
    path('setup/editar/<int:pk>', SetupUpdateView.as_view(), name='update_setup'),

    # Providers
    path('fornecedores/', ProviderListView.as_view(), name='providers'),
    path('fornecedor/novo', ProviderCreateView.as_view(), name='new_provider'),
    path('fornecedor/editar/<int:pk>', ProviderUpdateView.as_view(), name='update_provider'),

    # Products
    path('produtos/', ProductListView.as_view(), name='products'),
    path('produto/novo', ProductCreateView.as_view(), name='new_product'),
    path('produto/editar/<int:pk>', ProductUpdateView.as_view(), name='update_product'),
    path('produto/estimativa/<int:pk>', product_estimate, name='estimate_product'),

    # Traffic
    # path('trafego/', ProductListView.as_view(), name='traffic'),
    # path('trafego/novo', ProductCreateView.as_view(), name='new_traffic'),
    # path('trafego/editar/<int:pk>', ProductUpdateView.as_view(), name='update_traffic'),

    path('trafego/', TrafficListView.as_view(), name='traffic'),
    path('trafego/novo', TrafficCreateView.as_view(), name='new_traffic'),
    path('trafego/editar/<int:pk>', TrafficUpdateView.as_view(), name='update_traffic'),

    # Orders
    path('vendas/', OrderListView.as_view(), name='orders'),

    # Customers
    path('clientes/', CustomerListView.as_view(), name='customers'),

    # Traffic
    path('devolucoes/', DevolutionsListView.as_view(), name='devolutions'),

    # Support
    path('suporte/', support_index_view, name='support'),
]
