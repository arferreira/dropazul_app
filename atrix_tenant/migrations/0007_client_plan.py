# Generated by Django 2.0.5 on 2018-06-06 12:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('atrix_tenant', '0006_plan_purchase'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='plan',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='atrix_tenant.Plan'),
            preserve_default=False,
        ),
    ]
