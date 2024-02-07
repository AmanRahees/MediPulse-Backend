from django.db import models
from django.contrib.postgres.fields import ArrayField
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
    phone = models.BigIntegerField()
    picture = models.ImageField(upload_to="pictures/")
    gender = models.CharField(default="Male")
    speciality = models.ForeignKey(Speciality, on_delete=models.SET_NULL, null=True, blank=True)
    consultation_fee = models.IntegerField(default=500)
    services = ArrayField(models.CharField(max_length=200), blank=True, null=True)
    about = models.TextField()
    location = models.CharField(max_length=500)
    education = models.ManyToManyField(Educations, blank=True)
    experience = models.ManyToManyField(Experiences, blank=True)
    awards = models.ManyToManyField(Awards, blank=True)
    schedules = models.ManyToManyField(Schedules, blank=True)
    
    def __str__(self):
        return f"{self.account.email} --> {self.name}"
    
    class Meta:
        verbose_name_plural = "DOCTORS"
        ordering = ("-id",)
    
class Clinic(models.Model):
    doctor = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    clinic_address = models.CharField(max_length=500)
    clinic_images = models.ManyToManyField(Images)