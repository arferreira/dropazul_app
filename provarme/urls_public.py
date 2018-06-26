from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
# url para a landing page
from provarme_landing import urls as landing_urls
from provarme_site import urls as site_urls
from provarme_tenant import urls_public as tenant_urls
from provarme_dashboard import urls as dashboard_urls
from provarme_tenant.views import TenantRegisterView
from provarme import settings

from tenant_schemas.utils import connection

# interceptando se é inquelino ou se é publico



urlpatterns = [
    # root route - Landing page
    path('', include(landing_urls, namespace='landing-page')),
    # root route - site page
    path('site/', include(site_urls, namespace='site')),
    # rota para tenants
    path('cliente/', include(tenant_urls, namespace='tenant')),
    # rota para dashboard
    path('dashboard/', include(dashboard_urls, namespace='dashboard')),
    # admin django route
    path('manage/', admin.site.urls),

]


urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns