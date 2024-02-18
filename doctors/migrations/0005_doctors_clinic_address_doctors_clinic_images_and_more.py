# Generated by Django 5.0.1 on 2024-02-16 10:48

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0004_remove_clinic_clinic_images_clinic_clinic_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors',
            name='clinic_address',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='doctors',
            name='clinic_images',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.ImageField(upload_to='images/'), blank=True, null=True, size=None),
        ),
        migrations.AddField(
            model_name='doctors',
            name='clinic_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='location',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='doctors',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='pictures/'),
        ),
        migrations.DeleteModel(
            name='Clinic',
        ),
    ]