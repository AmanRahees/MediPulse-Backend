from django.db import models
from accounts.models import Accounts

class ClinicImages(models.Model):
    clinic_image = models.ImageField(upload_to="clinic_images")

class Schedules(models.Model):
    day = models.CharField(max_length=50)
    start_time = models.TimeField()
    end_time = models.TimeField()
    
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