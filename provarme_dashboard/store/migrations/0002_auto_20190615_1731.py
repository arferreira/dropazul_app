# Generated by Django 2.0.5 on 2019-06-15 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='status',
            field=models.BooleanField(choices=[(1, 'Ativa'), (2, 'Inativa')], default=True, verbose_name='Situação'),
        ),
    ]