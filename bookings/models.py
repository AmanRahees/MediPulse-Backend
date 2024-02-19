from django.db import models
from doctors.models import *
from base.models import *

# Create your models here.

class Appointments(models.Model):
    patient = models.ForeignKey(Patients, on_delete=models.SET_NULL, null=True, blank=True)
    doctor = models.ForeignKey(Doctors, on_delete=models.SET_NULL, null=True, blank=True)
    price = models.IntegerField(default=0)
    appointment_time = models.DateTimeField()
    booked_time = models.DateTimeField(auto_now_add=True)
    reason = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=100, default="pending")
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.patient.first_name} -> {self.doctor.name}"
    
    class Meta:
        verbose_name_plural = "APPOINTMENTS"
        ordering = ("-id",)

class BookingPayments(models.Model):
    appointment = models.ForeignKey(Appointments, on_delete=models.SET_NULL, null=True, blank=True)
    transaction_id = models.CharField(max_length=100)
    amount = models.IntegerField(default=0)
    status = models.CharField(max_length=100, default="paid")
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.appointment.id} -> {self.transaction_id}"