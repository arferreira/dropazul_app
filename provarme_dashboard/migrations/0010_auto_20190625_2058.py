# Generated by Django 2.0.5 on 2019-06-25 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provarme_dashboard', '0009_auto_20190625_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='settle',
            field=models.BooleanField(choices=[(True, 'Pago'), (False, 'Não Pago')], default=False, verbose_name='Liquidar'),
        ),
    ]