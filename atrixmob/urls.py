from django.contrib import admin
from django.conf.urls.static import static
from django.urls import path, include

# url para a landing page
from atrix_landing import urls as landing_urls
from atrix_tenant import urls as tenant_urls
from atrix_tenant.views import TenantRegisterView
from atrixmob import settings

urlpatterns = [
    # root route - Landing page
    path('', include(landing_urls, namespace='landing-page')),
    path('tenant/', include(tenant_urls, namespace='tenant')),
    #path('tenant/', TenantRegisterView.as_view()),
    # admin django route
    path('admin/', admin.site.urls),
]

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)