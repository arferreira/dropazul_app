# Generated by Django 2.0.5 on 2019-06-23 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('provarme_dashboard', '0005_devolution_traffic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devolution',
            name='address',
        ),
        migrations.RemoveField(
            model_name='devolution',
            name='city',
        ),
        migrations.RemoveField(
            model_name='devolution',
            name='state',
        ),
        migrations.RemoveField(
            model_name='devolution',
            name='zipcode',
        ),
    ]