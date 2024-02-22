# Generated by Django 5.0.1 on 2024-02-20 11:24

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0003_alter_doctors_services'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='services',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=list, size=None),
        ),
    ]
