# Generated by Django 2.0.5 on 2018-06-07 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atrix_tenant', '0007_client_plan'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Cliente', 'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterModelOptions(
            name='plan',
            options={'verbose_name': 'Plano', 'verbose_name_plural': 'Planos'},
        ),
        migrations.AlterModelOptions(
            name='purchase',
            options={'ordering': ['-created_on'], 'verbose_name': 'Compra', 'verbose_name_plural': 'Compras'},
        ),
        migrations.AddField(
            model_name='client',
            name='acceptance',
            field=models.BooleanField(default=False, verbose_name='Aceito os termos'),
        ),
        migrations.AddField(
            model_name='client',
            name='address',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Endereço'),
        ),
        migrations.AddField(
            model_name='client',
            name='address_number',
            field=models.CharField(blank=True, default='', max_length=20, null=True, verbose_name='Número'),
        ),
        migrations.AddField(
            model_name='client',
            name='city',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Cidade'),
        ),
        migrations.AddField(
            model_name='client',
            name='document',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='CNPJ ou CPF'),
        ),
        migrations.AddField(
            model_name='client',
            name='neighborhood',
            field=models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Bairro'),
        ),
        migrations.AddField(
            model_name='client',
            name='phone_number',
            field=models.CharField(default=1, max_length=20, verbose_name='Número de Telefone'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='client',
            name='province',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Estado/Província'),
        ),
        migrations.AddField(
            model_name='client',
            name='zipcode',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='CEP'),
        ),
        migrations.AlterField(
            model_name='client',
            name='is_active',
            field=models.BooleanField(default=False, verbose_name='Ativo?'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=500, verbose_name='Nome'),
        ),
        migrations.AlterField(
            model_name='client',
            name='name_fantasy',
            field=models.CharField(max_length=500, verbose_name='Nome de Fantasia'),
        ),
        migrations.AlterField(
            model_name='client',
            name='plan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='atrix_tenant.Plan', verbose_name='Plano contratado'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='amount',
            field=models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='description',
            field=models.CharField(max_length=500, verbose_name='Descrição'),
        ),
        migrations.AlterField(
            model_name='plan',
            name='name',
            field=models.CharField(max_length=500, verbose_name='Nome'),
        ),
    ]