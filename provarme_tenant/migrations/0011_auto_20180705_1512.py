# Generated by Django 2.0.5 on 2018-07-05 15:12

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provarme_tenant', '0010_auto_20180628_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='validate_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 8, 4, 15, 12, 49, 40776), verbose_name='Valido até'),
        ),
    ]
