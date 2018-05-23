from django.conf.urls import url
from django.urls import path, include, re_path

from atrix_tenant.views import TenantRegisterView, Login, Logout, activate

app_name="atrix_tenant"

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name="logout"),
    # rota para ativação do tenant
    path('activate/<int:id>/<token>/', activate, name='activate'),
]