# Generated by Django 5.0.1 on 2024-02-15 14:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0002_doctors_is_approved'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clinic',
            old_name='name',
            new_name='clinic_name',
        ),
    ]
