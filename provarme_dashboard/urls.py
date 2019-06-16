from django.conf.urls import url
from django.urls import path, include


# views Dashboard
from provarme_dashboard.dashboard.views import IndexView as dashboard_index


from provarme_dashboard.views import *



app_name="provarme_dashboard"

urlpatterns = [
    # Rota principal do dashboard
    path('', dashboard_index.as_view(), name='index'),

    # Store
    path('loja/', StoreListView.as_view(), name='stores'),
    path('loja/nova', StoreCreateView.as_view(), name='new_store'),
    path('loja/editar/<int:pk>', StoreUpdateView.as_view(), name='update_store'),


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






]