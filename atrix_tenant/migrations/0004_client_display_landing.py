# Generated by Django 2.0.5 on 2018-05-22 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atrix_tenant', '0003_client_display_site'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='display_landing',
            field=models.BooleanField(default=False),
        ),
    ]
