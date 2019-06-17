import random, string

from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, send_mail, mail_admins
from django.template.loader import render_to_string
from django.contrib.auth import login, logout
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.encoding import force_text, force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View, ListView, DeleteView, RedirectView
from django.shortcuts import render
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from django.http import JsonResponse
from provarme import settings


from pagseguro import PagSeguro

from tenant_schemas.utils import schema_exists, schema_context, connection





from provarme_tenant.forms import LoginForm
from provarme_tenant.models import Client, Plan, Purchase

# parse url
from provarme_tenant.tokens import account_activation_token





# ===================================================
# Checar se o schema já existe
# ===================================================

def validate_tenant(request):
    tenant_name = request.GET.get('subdomain', None);
    tenant_name = tenant_name.lower().replace(' ', '')
    if schema_exists(tenant_name):
        data = {
            'exist': True,
            'tenant_name': tenant_name.replace('provarme_', '')
        }
    else:
        data = {
            'exist': False,
            'tenant_name': tenant_name.replace('provarme_', '')
        }

    return JsonResponse(data)


# ===================================================
# Login de Inquilinos
# ===================================================

class Login(View):
    template_name = "provarme_tenant/login_tenant.html"
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
    template_name = "provarme_tenant/register_tenant.html"
    active_menu = "register"
    plans = Plan.objects.all()

    def get(self, request):
        return render(request, self.template_name, {'active_menu': self.active_menu, 'plans': self.plans})


    def post(self, request):
        kwargs = {
            'url_login_new_schema': None,
            'form_data': request.POST
        }
        tenant_name = request.POST.get('tenant_name', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        plan = request.POST.get('plan', None)
        name_fantasy = request.POST.get('name_fantasy', None)
        if schema_exists(tenant_name):
            print('O inquilino já foi criado!')
            kwargs['tenant_exist'] = True
        else:
            print('Criando inquilino para o atrix')
            client = Client()
            client.domain_url = '{0}.{1}'.format(tenant_name, request.tenant.domain_url)
            client.name = tenant_name
            client.name_fantasy = name_fantasy
            client.is_active = True
            client.schema_name = 'atrix_' + tenant_name
            client.save()
            # Executando as migrações
            with schema_context('atrix_' + tenant_name):
                print('Rodando as migrações com o Cliente que foi criado!')
                user = User()
                user.email = email
                user.username = name_fantasy
                user.set_password(password)
                user.is_active = False
                user.is_staff= False
                user.is_superuser = False
                user.save()
                # Montando estrutura de email
                active_url = '{0}.{1}'.format(tenant_name, get_current_site(request))
                active_url = active_url.replace("www.", "")
                mail_subject = '[provarme_core] - Inicie sua instância do provarme_core.'
                to_email = email
                plain_text = render_to_string('provarme_tenant/email_notification/tenant_active_email.html', {
                    'user': user,
                    'domain': active_url,
                    'id': user.pk,
                    'token': account_activation_token.make_token(user),
                })
                message_html = render_to_string('provarme_tenant/email_notification/tenant_active_email.html', {
                    'user': user,
                    'domain': active_url,
                    'id': user.pk,
                    'token': account_activation_token.make_token(user),
                })
                # TODO: Refatorar envio de email para ativação de instancia e testsssss
                print('Enviando email para o cliente de ativação de instancia')
                # Enviando email de criação da instancia

                try:
                    send_mail(
                        mail_subject,
                        plain_text,
                        'contato.provarme_core@provarme_core.com.br',
                        [to_email],
                        html_message=message_html,
                        fail_silently=False
                    )
                except Exception as e:
                    print('O email não foi enviado, erro: ', e)

                mail_admins(
                    'Notificação - Você possui um novo contratante do sistema',
                    '%s criou cadastro agora no provarme_core.' % active_url,
                    fail_silently=False
                )
                url_redirect = "{0}.{1}{2}".format(
                    tenant_name, request.META['HTTP_HOST'], reverse('tenant:register')
                )
            response = {
                'exist': True,
                'tenant_exist': True,
                'url_login_new_schema': url_redirect
            }
            print('Criação finalizada!')
        return JsonResponse(response)


# ===================================================
# Ativação de Inquilinos
# ===================================================

def activate(request, id, token, schema_name):
    with schema_context(schema_name):
        try:
            user = User.objects.get(pk=id)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.is_staff = False
            user.is_superuser = True
            user.save()
            #login(request, user)
            # return redirect('home')
            return render(request, 'provarme_tenant/tenant_active.html')
        else:
            return render(request, 'provarme_tenant/tenant_invalid.html')



# ===================================================
# Perfil do Inquilino
# ===================================================

class TenantProfile(LoginRequiredMixin, View):
    template_name = "provarme_tenant/tenant_profile.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        tenantprofile = request.user.profile
        image_profile = request.FILES['image_profile'] if 'image_profile' in request.FILES else None
        if image_profile:
            tenantprofile.image_profile = image_profile
            tenantprofile.save()
        request.user.username = request.POST['email']
        request.user.first_name = request.POST['first_name']
        request.user.last_name = request.POST['last_name']
        request.user.email = request.POST['email']
        request.user.save()
        return HttpResponseRedirect(reverse_lazy('dashboard:index'))



# ===================================================
# Assinatura de Inquilinos
# ===================================================


class TenantSignatureView(RedirectView):
    template_name = "provarme_tenant/signature_tenant.html"
    plans = Plan.objects.all()

    def get(self, request):
        return render(request, self.template_name, {'plans': self.plans})


    def post(self, request):
        kwargs = {
            'url_login_new_schema': None,
            'form_data': request.POST
        }

        tenant_name = request.POST.get('subdomain', None)
        name_fantasy = request.POST.get('name_fantasy', None)
        email = request.POST.get('email', None)
        phone_number = request.POST.get('phone_number', None)
        area_code = phone_number[1:3]
        phone = phone_number[5:15]
        phone = phone.replace('-', '')
        password = request.POST.get('password', None)
        plan = request.POST.get('plan', None)


        if schema_exists(tenant_name):
            print('O inquilino já foi criado!')
            kwargs['tenant_exist'] = True
        else:
            print('Criando inquilino para o provarme')
            client = Client()
            site_url = request.tenant.domain_url.replace('www.', '')
            client.domain_url = '{0}.{1}'.format(tenant_name, site_url)
            client.name = tenant_name
            client.name_fantasy = name_fantasy
            client.is_active = False
            client.schema_name = 'provarme_' + tenant_name
            client.save()

            # Criando a compra para o cliente
            purchase = Purchase()
            purchase.plan = Plan.objects.get(pk=plan)
            purchase.client = client
            purchase.active_url = '{0}.{1}'.format(tenant_name, site_url)
            purchase.save()

            # Executando as migrações
            with schema_context('provarme_' + tenant_name):
                print('Rodando as migrações com o Cliente que foi criado!')
                user = User()
                user.email = email
                user.username = name_fantasy
                user.set_password(password)
                user.is_active = False
                user.is_staff= False
                user.is_superuser = False
                user.save()
                # Lógica para o pagamento do plano e assinatura
                config = { 'sandbox': True }
                pg = PagSeguro(email='antonioricardo_ferreira@hotmail.com', token='51E3688E0039466ABF8FEDDA8BD9A687',
                               config=config)
                pg.sender = {
                    "name": name_fantasy,
                    "area_code": area_code,
                    "phone": phone,
                    "email": email
                }
                pg.reference_prefix = None
                pg.shipping = None
                pg.reference = purchase.pk
                pg.add_item(id=purchase.plan.pk, description=purchase.plan.description,
                            amount=purchase.plan.amount, quantity=1)
                pg.redirect_url = self.request.build_absolute_uri(
                    reverse('tenant:signature')
                )
                pg.notification_url = self.request.build_absolute_uri(
                    reverse('tenant:pagseguro_notification')
                )

                mail_admins(
                    'Notificação - Nova contratação do sistema',
                    'O sistema acabou de criar e aguarda pagamento da instancia: %s' % tenant_name,
                    fail_silently=False
                )
                response = pg.checkout()
            print('Criação finalizada!')
        return HttpResponseRedirect(response.payment_url)


@csrf_exempt
def pagseguro_notification(request):
    notification_code = request.POST.get('notificationCode', None)
    if notification_code:
        pg = PagSeguro(
            email=settings.PAGSEGURO_EMAIL, token=settings.PAGSEGURO_TOKEN,
            config={'sandbox': settings.PAGSEGURO_SANDBOX}
        )
        notification_data = pg.check_notification(notification_code)
        status = notification_data.status
        reference = notification_data.reference

        try:
            purchase = Purchase.objects.get(pk=reference)
        except Purchase.DoesNotExist:
            pass
        else:
            purchase.pagseguro_update_status(status)
    return HttpResponse('Pagamento atualizado!')