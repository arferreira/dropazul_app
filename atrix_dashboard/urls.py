from django.conf.urls import url
from django.urls import path, include


# views Dashboard
from atrix_dashboard.dashboard.views import IndexView as dashboard_index


from atrix_dashboard.views import *



app_name="atrix_dashboard"

urlpatterns = [
    # Rota principal do dashboard
    path('', dashboard_index.as_view(), name='index'),

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

    # Funcionarios
    path('colaboradores/', EmployeeListView.as_view(), name='employees'),
    path('colaborador/novo', EmployeeCreateView.as_view(), name='new_employee'),
    path('colaborador/editar/<int:pk>', EmployeeUpdateView.as_view(), name='update_employee'),
    path('colaborador/excluir/<int:employee_id>', employee_delete, name='delete_employee'),


    # Expedientes
    path('expedientes/', EmployeeListView.as_view(), name='office_hours'),
    path('expediente/novo', EmployeeCreateView.as_view(), name='new_office_hour'),
    path('expediente/editar/<int:pk>', EmployeeUpdateView.as_view(), name='update_office_hours'),
    path('expediente/excluir/<int:office_id>', employee_delete, name='delete_office_hours'),


    # Categorias
    # path('categorias/', CategoryListView.as_view(), name='categories'),
    # path('categoria/novo/', CategoryCreateView.as_view(), name='new_category'),
    # path('categoria/editar/<int:pk>', CategoryUpdateView.as_view(), name='update_category'),

    # # Produtos
    # url(r'produto/novo/$', AddProductView.as_view(), name='new_product'),
    # url(r'produtos/$', ProductListView.as_view(), name='products'),
    # url(r'produtos/baixoestoque/$', ProductLowStockListView.as_view(), name='products_lowstock'),
    # url(r'produto/editar/(?P<pk>[0-9]+)/$', UpdateProductView.as_view(), name='update_product'),
    # url(r'^estoque/', include('atrix_dashboard.stock.urls')),

]