from django.urls import path, re_path
from django.conf.urls import url

from provarme_tenant.views import (TenantRegisterView, TenantSignatureView, Login, Logout,
                                   validate_tenant, activate, pagseguro_notification, create_purchase_upnid)

app_name="provarme_tenant"

urlpatterns = [
    # root route
    path('criacao/', TenantSignatureView.as_view(), name='signature'),
    # atualizando status de pagamento de planos
    path('assinatura/retorno/', pagseguro_notification, name='pagseguro_notification'),
    #  Requisições ajax de validação de instancia
    path('ajax/validando_cliente/', validate_tenant, name='validate_tenant'),
    # rota para ativação do tenant
    path('ativar/<int:id>/<token>/<schema_name>/', activate, name='activate'),
    path('entrar/', Login.as_view(), name='login'),
    path('sair/', Logout.as_view(), name="logout"),
]