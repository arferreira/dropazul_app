from django.urls import path, re_path
from django.conf.urls import url

from atrix_tenant.views import (TenantRegisterView, Login, Logout, validate_tenant, activate)

app_name="atrix_tenant"

urlpatterns = [
    # root route
    path('register/', TenantRegisterView.as_view(), name='register'),
    #  Requisições ajax
    path('ajax/validate_tenant/', validate_tenant, name='validate_tenant'),
    # rota para ativação do tenant
    path('activate/<int:id>/<token>/', activate, name='activate'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name="logout"),
]