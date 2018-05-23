import random, string

from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.auth import login, logout
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.encoding import force_text, force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic import View, ListView, DeleteView
from django.shortcuts import render
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.http import JsonResponse

from tenant_schemas.utils import schema_exists, schema_context, connection


# parse url
from tld import get_tld
from tld.utils import update_tld_names


from atrix_tenant.forms import LoginForm
from atrix_tenant.models import Client
from atrix_core.json_settings import get_settings

# parse url
from atrix_tenant.tokens import account_activation_token

update_tld_names()

settings = get_settings()

# ===================================================
# Checar se o schema já existe
# ===================================================

def validate_tenant(request):
    tenant_name = request.GET.get('subdomain', None);
    print(tenant_name)
    if schema_exists(tenant_name):
        data = {
            'exist': True
        }
    else:
        data = {
            'exist': False
        }

    return JsonResponse(data)


# ===================================================
# Login de Inquilinos
# ===================================================

class Login(View):
    template_name = "atrix_tenant/login_tenant.html"
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
        return HttpResponseRedirect(reverse_lazy('site:index'))


# ===================================================
# Registro de Inquilinos
# ===================================================


class TenantRegisterView(View):
    template_name = "atrix_tenant/register_tenant.html"
    active_menu = "register"

    def get(self, request):
        return render(request, self.template_name, {'active_menu': self.active_menu})


    def post(self, request):
        kwargs = {
            'active_menu': self.active_menu,
            'url_login_new_schema': None,
            'form_data': request.POST
        }
        tenant_name = request.POST.get('tenant_name', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        name_fantasy = request.POST.get('name_fantasy', None)
        if schema_exists(tenant_name):
            kwargs['tenant_exist'] = True
        else:
            client = Client()
            client.domain_url = '{0}.{1}'.format(tenant_name, request.tenant.domain_url)
            client.name = tenant_name
            client.name_fantasy = name_fantasy
            client.is_active = True
            client.schema_name = 'atrix_' + tenant_name
            client.save()  # Executando as migrações
            with schema_context('atrix_' + tenant_name):
                user = User()
                user.email = email
                user.username = email
                user.set_password(password)
                user.is_active = False
                user.is_staff= False
                user.is_superuser = False
                user.save()
                url_activate = "{0}.{1}".format(
                    tenant_name, request.META['HTTP_HOST']
                )

                mail_subject = 'Ative sua instância do atrixmob.'

                message = render_to_string('atrix_tenant/tenant_active_email.html', {
                    'user': user,
                    'domain': url_activate,
                    'id': user.pk,
                    'token': account_activation_token.make_token(user),
                })

                to_email = email
                email = EmailMessage(
                    mail_subject, message, to=[to_email]
                )
                email.send()
                url_redirect = "{0}.{1}{2}".format(
                    tenant_name, request.META['HTTP_HOST'], reverse('tenant:register')
                )
            response = {
                'exist': True,
                'tenant_exist': True,
                'url_login_new_schema': url_redirect
            }
        return JsonResponse(response)


# ===================================================
# Ativação de Inquilinos
# ===================================================

def activate(request, id, token):
    try:
        user = User.objects.get(pk=id)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.is_staff = False
        user.is_superuser = True
        user.save()
        login(request, user)
        # return redirect('home')
        return render(request, 'atrix_tenant/tenant_active.html')
    else:
        return render(request, 'atrix_tenant/tenant_invalid.html')