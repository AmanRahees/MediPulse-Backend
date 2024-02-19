from django.dispatch import receiver
from django.db.models.signals import post_save
from accounts.models import Accounts
from base.models import Patients, Wallet
from doctors.models import Doctors

@receiver(post_save, sender=Accounts)
def register_accout(sender, instance, created, **kwargs):
    if created and instance.role != "admin":
        if instance.role == "doctor":
            Doctors.objects.create(account=instance, name = instance.username)
        else:
            Patients.objects.create(account=instance, first_name = instance.username.split()[0])
        Wallet.objects.create(account=instance)