from django.db import models
from django.contrib.postgres.fields import ArrayField
from datetime import datetime, timedelta, date
from contexts.models import *

# Create your models here.

class Speciality(models.Model):
    speciality_name = models.CharField(max_length=200)
    speciality_image = models.ImageField(upload_to="specialities/")
    description = models.TextField()
    
    def __str__(self):
        return self.speciality_name
    
    class Meta:
        verbose_name_plural = "SPECIALITIES"

class Doctors(models.Model):
    name = models.CharField(max_length=200)
    account = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    phone = models.BigIntegerField(null=True, blank=True)
    picture = models.ImageField(upload_to="pictures/", null=True, blank=True)
    gender = models.CharField(default="Male")
    speciality = models.ForeignKey(Speciality, on_delete=models.SET_NULL, null=True, blank=True)
    consultation_fee = models.IntegerField(default=500)
    services = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    about = models.TextField()
    location = models.CharField(max_length=500, null=True, blank=True)
    clinic_name = models.CharField(max_length=200, null=True, blank=True)
    clinic_address = models.CharField(max_length=500, null=True, blank=True)
    clinic_images = models.ManyToManyField(ClinicImages, blank=True)
    education = models.ManyToManyField(Educations, blank=True)
    experience = models.ManyToManyField(Experiences, blank=True)
    awards = models.ManyToManyField(Awards, blank=True)
    schedules = models.ManyToManyField(Schedules, blank=True)
    slot_duration = models.CharField(max_length=100, default="10 mins")
    is_approved = models.BooleanField(default=False)
    
    def __str__(self):
        return f"Dr. {self.name}"
    
    class Meta:
        verbose_name_plural = "DOCTORS"
        ordering = ("-id",)
    
class Slots(models.Model):
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    is_booked = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.end_time:
            self.end_time = (datetime.combine(date.today(), self.start_time) + timedelta(minutes=self.doctor.slot_duration)).time()
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name_plural = "SLOTS"
        ordering = ("-id",)