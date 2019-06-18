from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import path, include, re_path

from provarme_tenant.views import (TenantRegisterView, Login, Logout, activate, TenantProfile, PendingPageView, ThankPageView)
from provarme import settings

app_name="provarme_tenant"

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name="logout"),
    # rota para ativação do tenant
    path('activate/<int:id>/<token>/', activate, name='activate'),
    # rota para perfil do usuario tenant
    path('profile/', TenantProfile.as_view(), name='profile'),
    path('obrigado/', ThankPageView.as_view(), name='thank'),
    path('pendente/', PendingPageView.as_view(), name='pending'),
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)