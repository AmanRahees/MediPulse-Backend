from django.db import models
from accounts.models import Accounts

# Create your models here.

class Patients(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200, null=True, blank=True)
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    phone = models.BigIntegerField(null=True, blank=True)
    picture = models.ImageField(upload_to="pictures/", null=True)
    gender = models.CharField(default="Male")
    DOB = models.DateField(null=True, blank=True)
    blood_group = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"#P100{self.id}"

    class Meta:
        verbose_name_plural = "PATIENTS"
        ordering = ("-id",)

class Transactions(models.Model):
    paid_from = models.ForeignKey(Accounts, on_delete=models.SET_NULL, null=True, blank=True, related_name='transactions_paid_from')
    paid_to = models.ForeignKey(Accounts, on_delete=models.SET_NULL, null=True, blank=True, related_name='transactions_paid_to')
    amount = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    transaction_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "TRANSACTIONS"
        ordering = ("-id",)

class Wallet(models.Model):
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    balance = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    transactions = models.ManyToManyField(Transactions, blank=True)

    class Meta:
        verbose_name_plural = "WALLET"