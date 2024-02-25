from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from doctors.models import Doctors, SlotInstance, Slots
from datetime import datetime, timedelta
from doctors.func import get_day_of_week

@receiver(pre_save, sender=Doctors)
def handle_slot_duration(sender, instance, **kwargs):
    if not kwargs.get('created', False):
        obj = Doctors.objects.get(pk=instance.pk)
        if obj.slot_duration != instance.slot_duration:
            instance.schedules.all().update(slot_duration=instance.slot_duration)
            for schedule in instance.schedules.all():
                schedule.save()

@receiver(post_save, sender=SlotInstance)
def create_slots(sender, instance, created, **kwargs):
    if created:
        schedule = instance.doctor.schedules.filter(day=get_day_of_week(instance.date)).first()
        if schedule:
            slot_duration = instance.doctor.slot_duration
            start_time = schedule.start_time
            total_slots = schedule.total_slots
            for i in range(total_slots):
                Slots.objects.create(
                    slot_instance=instance,
                    date = instance.date,
                    start_time = start_time
                )
                start_time = (datetime.combine(datetime.today(), start_time) + timedelta(minutes=slot_duration)).time()