import random, string
from django.template.loader import render_to_string
from django.contrib.auth import login, logout
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.views.generic import View, ListView, DeleteView
from django.shortcuts import render
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from tenant_schemas.utils import schema_exists, schema_context, connection

# parse url
from tld import get_tld
from tld.utils import update_tld_names


from atrix_tenant.forms import LoginForm
from atrix_tenant.models import Client
from atrix_core.json_settings import get_settings

# parse url
update_tld_names()

settings = get_settings()


# ===================================================
# Login de Inquilinos
# ===================================================

class Login(View):
    template_name = "atrix_core/login_tenant.html"
    form = LoginForm

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('dashboard:index'))
        else:
            ctx = {'form': self.form, 'tenant': connection.tenant}
            if 'next' in request.GET:
                ctx['next'] = request.GET['next']
            return render(request, self.template_name, ctx)

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            login(request, form.my_user)
            messages.success(request, _("Bem vindo {0}!".format(form.my_user.first_name)))
            if 'next' in request.POST:
                return HttpResponseRedirect(request.POST['next'])
            else:
                return HttpResponseRedirect(reverse_lazy('dashboard:index'))
        else:
            ctx = {'form': form}
            return render(request, self.template_name, ctx)




# ===================================================
# Logout de Inquilinos
# ===================================================

class Logout(View):

    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse_lazy('landing-page:home'))


# ===================================================
# Registro de Inquilinos
# ===================================================


class TenantRegisterView(View):
    template_name = "atrix_core/register_tenant.html"
    active_menu = "register"

    def get(self, request):
        return render(request, self.template_name, {'active_menu': self.active_menu})


    def post(self, request):
        kwargs = {
            'active_menu': self.active_menu,
            'url_login_new_schema': None,
            'form_data': request.POST
        }
        tenant_name = request.POST.get('subdomain')
        email = request.POST.get('email')
        password = request.POST.get('password')
        name_fantasy = request.POST.get('name_fantasy')
        if schema_exists(tenant_name):
            kwargs['tenant_exist'] = True
        else:
            client = Client()
            client.domain_url = '{0}.{1}'.format(tenant_name, request.tenant.domain_url)
            client.name = tenant_name
            client.name_fantasy = name_fantasy
            client.schema_name = 'atrix_' + tenant_name
            client.save()  # Executando as migrações
            with schema_context('atrix_' + tenant_name):
                user = User()
                user.email = email
                user.username = email
                user.set_password(password)
                user.is_active = True
                user.is_staff= True
                user.is_superuser = True
                user.save()
                url_redirect = "{0}.{1}{2}".format(
                tenant_name, request.META['HTTP_HOST'].split('.')[1], reverse('tenant:login')
                )
                print(request.META['HTTP_HOST'].split('.')[1])
                print(tenant_name)
                print(url_redirect)
            kwargs['tenant_exist'] = True
            kwargs['url_login_new_schema'] = url_redirect
        return render(request, self.template_name, kwargs)