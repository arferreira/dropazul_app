from django.db import models



KIND_CUSTOMER = (
    (1, 'Pessoa Física'),
    (2, 'Pessoa Jurídica'),
)

# Modelo para clientes
class Customer(models.Model):
    kind = models.IntegerField(default=1, choices=KIND_CUSTOMER, verbose_name='Tipo de cliente',
                               blank=False, null=False)
    # Pessoa Física
    name_social_name = models.CharField(blank=False, null=False, verbose_name='Nome / Razão Social',
                                        max_length=500)
    cpf = models.CharField(max_length=20, blank=True, null=True, verbose_name='CPF')
    rg = models.CharField(max_length=50, blank=True, null=True, verbose_name='RG')
    born_date = models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')
    email = models.CharField(max_length=255, verbose_name='Email')
    phone_number = models.CharField(max_length=20, verbose_name='Número de Telefone')

    # Pessoa Juridica
    name_fantasy = models.CharField(max_length=500, null=True, blank=True, verbose_name='Nome de Fantasia')
    cnpj = models.CharField(max_length=500, null=True, blank=True, verbose_name='CNPJ')
    responsible = models.CharField(max_length=500, null=True, blank=True, verbose_name='Responsável')

    # Dados de Endereço
    zipcode = models.CharField(max_length=10, blank=True, null=True, verbose_name="CEP")

    city = models.CharField(max_length=100, blank=True, null=True, verbose_name="Cidade")

    province = models.CharField(max_length=100, blank=True, null=True, verbose_name="Estado/Província")

    address = models.CharField(max_length=100, blank=True, null=True, default='', verbose_name="Endereço")

    address_number = models.CharField(max_length=20, blank=True, null=True, default='', verbose_name="Número")

    neighborhood = models.CharField(max_length=100, blank=True, null=True, default='', verbose_name="Bairro")

    # Informações adicionais
    aditional_information = models.TextField(verbose_name='Informações Adicionais', null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Criado em')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Modificado em')


    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


    def __str__(self):
        return self.name_social_name

