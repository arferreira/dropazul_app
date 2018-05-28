import os

from django.db import models, connection
from django.utils.text import slugify
from tenant_schemas.models import TenantMixin
from django.contrib.auth.models import User

class Client(TenantMixin):
    name = models.CharField(max_length=500)
    name_fantasy = models.CharField(max_length=500)
    is_active = models.BooleanField(default=False)
    display_site = models.BooleanField(default=False)
    display_landing = models.BooleanField(default=False)
    created_on = models.DateField(auto_now_add=True)

    # automaticamente o sistema criara as migraçoes a cada tenant criado
    auto_create_schema = True


class Profile(models.Model):
    def image_path(self, filename):
        extension = os.path.splitext(filename)[1][1:]
        file_name = os.path.splitext(filename)[0]
        url = "%s/Users/%s/profile/%s.%s" % (
        connection.tenant.domain_url, self.user.id, slugify(str(file_name)), extension)
        return url

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    cellphone = models.CharField(max_length=20)
    # Dados empresariais
    cnpj = models.CharField(max_length=40)
    cpf = models.CharField(max_length=40)
    image_profile = models.ImageField(upload_to=image_path, null=True, blank=True)


    def __str__(self):
        return self.user.get_full_name()



# ============================================================
# Conectamos os signals
# ============================================================

from .signals import *