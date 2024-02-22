from django.db import models
from datetime import datetime, timedelta
from accounts.models import Accounts

class ClinicImages(models.Model):
    clinic_image = models.ImageField(upload_to="clinic_images")
    
DAY_CHOICES = [
    ("MONDAY", "MONDAY"),
    ("TUESDAY", "TUESDAY"),
    ("WEDNESDAY", "WEDNESDAY"),
    ("THURSDAY", "THURSDAY"),
    ("FRIDAY", "FRIDAY"),
    ("SATURDAY", "SATURDAY"),
    ("SUNDAY", "SUNDAY"),
]

class Schedules(models.Model):
    day = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField(null=True, blank=True)
    total_slots = models.IntegerField(default=5)
    slot_duration = models.IntegerField(default=10)

    def save(self, *args, **kwargs):
        start = datetime.strptime(str(self.start_time), '%H:%M:%S')
        duration = timedelta(minutes=self.slot_duration * self.total_slots)
        end = start + duration
        self.end_time = end.time()
        super().save(*args, **kwargs)
    
class Educations(models.Model):
    degree = models.CharField(max_length=200)
    institute = models.CharField(max_length=200)
    date_from = models.DateField()
    date_to = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.degree} - {self.institute}"

class Experiences(models.Model):
    hospital_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    date_from = models.DateField()
    date_to = models.DateField(null=True, blank=True)
    present = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.hospital_name} - {self.position} ({self.date_from}, {self.date_to})"
    
class Awards(models.Model):
    award_name = models.CharField(max_length=200)
    award_year = models.DateField()

    def __str__(self):
        return f"{self.award_name} ({self.award_year})"
    
class EmailVerification(models.Model):
    email = models.EmailField(unique=True)
    otp = models.IntegerField()
    is_verified = models.BooleanField(default=False)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.email
    
class Notifications(models.Model):
    user = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    message = models.TextField()
    read = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)