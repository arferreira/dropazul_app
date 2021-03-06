# Generated by Django 2.0.5 on 2019-06-15 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tx_shopify', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Taxa Shopify')),
                ('tx_gateway', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Taxa do Gateway')),
                ('tx_antecipation', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Taxa de Antecipação')),
                ('tx_tax', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Imposto')),
                ('tx_iof', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='IOF')),
                ('tx_cashback', models.DecimalField(decimal_places=2, max_digits=3, verbose_name='Cashback')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('status', models.BooleanField(choices=[(1, 'Ativa'), (2, 'Inativa')], default=True, verbose_name='Situação')),
            ],
            options={
                'verbose_name': 'Configurações',
            },
        ),
    ]
