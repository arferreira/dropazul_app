from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
# url para a landing page
from provarme_landing import urls as landing_urls
from provarme_site import urls as site_urls
from provarme_tenant import urls as tenant_urls
from provarme_dashboard import urls as dashboard_urls
from provarme_webhooks import urls as webhooks_urls
from provarme_tenant.views import TenantRegisterView, activate
from provarme import settings

from tenant_schemas.utils import connection

# interceptando se é inquelino ou se é publico



urlpatterns = [
    # root route - site page
    path('', include(site_urls, namespace='site')),
    # rota para tenants
    path('tenant/', include(tenant_urls, namespace='tenant')),
    # rota para dashboard
    path('painel/', include(dashboard_urls, namespace='dashboard')),
    # rota para webhooks
    path('webhooks/', include(webhooks_urls, namespace='webhooks')),
]


urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
