# Generated by Django 5.0.1 on 2024-02-22 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contexts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='schedules',
            name='total_slots',
            field=models.IntegerField(default=5),
        ),
    ]