# Generated by Django 5.0.1 on 2024-02-19 14:49

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(blank=True, max_length=200, null=True)),
                ('phone', models.BigIntegerField(blank=True, null=True)),
                ('picture', models.ImageField(upload_to='pictures/')),
                ('gender', models.CharField(default='Male')),
                ('DOB', models.DateField(blank=True, null=True)),
                ('blood_group', models.CharField(blank=True, max_length=50, null=True)),
                ('city', models.CharField(blank=True, max_length=100, null=True)),
                ('state', models.CharField(blank=True, max_length=100, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'PATIENTS',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('transaction_date', models.DateTimeField(auto_now_add=True)),
                ('paid_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transactions_paid_from', to=settings.AUTH_USER_MODEL)),
                ('paid_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='transactions_paid_to', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'TRANSACTIONS',
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default=0, max_digits=10)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('transactions', models.ManyToManyField(blank=True, to='base.transactions')),
            ],
            options={
                'verbose_name_plural': 'WALLET',
            },
        ),
    ]
