# Generated by Django 2.0.5 on 2019-06-25 18:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provarme_dashboard', '0007_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True, verbose_name='Nome')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Saldo')),
                ('balance_date', models.DateTimeField(blank=True, null=True, verbose_name='Data')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Criado em')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Atualizado em')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
