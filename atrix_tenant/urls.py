from django.urls import path, include

from atrix_tenant.views import TenantRegisterView, Login, Logout

app_name="atrix_tenant"

urlpatterns = [
    # root route
    path('register/', TenantRegisterView.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name="logout"),
]