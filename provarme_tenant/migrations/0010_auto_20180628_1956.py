# Generated by Django 2.0.5 on 2018-06-28 19:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provarme_tenant', '0009_auto_20180628_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='validate_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 28, 19, 56, 32, 47537), verbose_name='Valido até'),
        ),
    ]
