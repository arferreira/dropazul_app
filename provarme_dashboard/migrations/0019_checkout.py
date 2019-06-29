# Generated by Django 2.0.5 on 2019-06-28 21:16

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('provarme_dashboard', '0018_auto_20190628_1542'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modificado em')),
                ('deleted_at', models.DateTimeField(blank=True, null=True, verbose_name='Excluido em')),
                ('shopify_id', models.CharField(max_length=50, verbose_name='ID Shopify')),
                ('token', models.CharField(max_length=150, verbose_name='Token')),
                ('cart_token', models.CharField(max_length=150, verbose_name='Token do Carrinho')),
                ('email', models.CharField(max_length=150, verbose_name='Email')),
                ('checkout_url', models.CharField(max_length=255, verbose_name='Url')),
                ('body', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='checkouts', to='provarme_dashboard.Customer')),
            ],
            options={
                'verbose_name': 'Abandono',
                'verbose_name_plural': 'Abandonos',
                'ordering': ['-created_at'],
            },
        ),
    ]
