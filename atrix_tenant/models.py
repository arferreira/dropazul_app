from django.db import models
from tenant_schemas.models import TenantMixin

class Client(TenantMixin):
    name = models.CharField(max_length=500)
    name_fantasy = models.CharField(max_length=500)
    is_active = models.BooleanField(default=False)
    display_site = models.BooleanField(default=False)
    display_landing = models.BooleanField(default=False)
    created_on = models.DateField(auto_now_add=True)

    # automaticamente o sistema criara as migraçoes a cada tenant criado
    auto_create_schema = True