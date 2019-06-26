# Generated by Django 2.0.5 on 2019-06-26 00:50

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('provarme_dashboard', '0008_customer_customeraddress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopify_id', models.CharField(max_length=50, verbose_name='ID Shopify')),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=15, null=True)),
                ('financial_status', models.CharField(blank=True, max_length=255, null=True)),
                ('order_number', models.CharField(blank=True, max_length=255, null=True)),
                ('body', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='provarme_dashboard.Customer')),
            ],
            options={
                'verbose_name': 'Pedido',
                'verbose_name_plural': 'Pedidos',
            },
        ),
    ]
