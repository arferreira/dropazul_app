# Generated by Django 2.0.5 on 2018-06-08 00:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atrix_tenant', '0014_remove_client_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='validate_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 8, 0, 55, 57, 883745)),
        ),
    ]