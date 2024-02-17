# Generated by Django 5.0.1 on 2024-02-17 07:14

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0005_doctors_clinic_address_doctors_clinic_images_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='clinic_images',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(upload_to='images/'), blank=True, default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='services',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=200), blank=True, default=list, null=True, size=None),
        ),
    ]
