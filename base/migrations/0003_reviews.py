# Generated by Django 5.0.1 on 2024-02-24 14:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_alter_patients_picture'),
        ('doctors', '0005_alter_doctors_slot_duration'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=2, default=5, max_digits=3)),
                ('comment', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctors.doctors')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.patients')),
            ],
            options={
                'verbose_name_plural': 'REVIEWS',
            },
        ),
    ]
