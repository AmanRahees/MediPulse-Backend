from django.dispatch import receiver
from django.db.models.signals import pre_save
from doctors.models import Doctors

@receiver(pre_save, sender=Doctors)
def HandleSlotDuration(sender, instance, **kwargs):
    if not kwargs.get('created', False):
        obj = Doctors.objects.get(pk=instance.pk)
        if obj.slot_duration != instance.slot_duration:
            instance.schedules.all().update(slot_duration=instance.slot_duration)
            for schedule in instance.schedules.all():
                schedule.save()