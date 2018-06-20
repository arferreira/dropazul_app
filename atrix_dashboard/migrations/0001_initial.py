# Generated by Django 2.0.5 on 2018-06-18 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kind', models.IntegerField(choices=[(1, 'Pessoa Física'), (2, 'Pessoa Jurídica')], default=1, verbose_name='Tipo de cliente')),
                ('name_social_name', models.CharField(max_length=500, verbose_name='Nome / Razão Social')),
                ('cpf', models.CharField(blank=True, max_length=20, null=True, verbose_name='CPF')),
                ('rg', models.CharField(blank=True, max_length=50, null=True, verbose_name='RG')),
                ('born_date', models.DateField(blank=True, null=True, verbose_name='Data de Nascimento')),
                ('email', models.CharField(max_length=255, verbose_name='Email')),
                ('phone_number', models.CharField(max_length=20, verbose_name='Número de Telefone')),
                ('name_fantasy', models.CharField(blank=True, max_length=500, null=True, verbose_name='Nome de Fantasia')),
                ('cnpj', models.CharField(blank=True, max_length=500, null=True, verbose_name='CNPJ')),
                ('responsible', models.CharField(blank=True, max_length=500, null=True, verbose_name='Responsável')),
                ('zipcode', models.CharField(blank=True, max_length=10, null=True, verbose_name='CEP')),
                ('city', models.CharField(blank=True, max_length=100, null=True, verbose_name='Cidade')),
                ('province', models.CharField(blank=True, max_length=100, null=True, verbose_name='Estado/Província')),
                ('address', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Endereço')),
                ('address_number', models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='Número')),
                ('neighborhood', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Bairro')),
                ('aditional_information', models.TextField(verbose_name='Informações Adicionais')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]