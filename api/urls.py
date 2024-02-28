from django.urls import path
from base.views import *
from bookings.views import *

urlpatterns = [
    # doctors
    path("doctors", ListDoctors.as_view(), name="list-doctors"),
    path("doctors/<int:pk>", DoctorPreview.as_view(), name="preview-doctor"),
    path("doctors/<int:doctor_id>/slots/<str:date>", ListSlots.as_view(), name="list-doctor-slots"),

    # bookings
    path("bookings/payment", BookingAPI.as_view(), name="booking-payment-api"),

    # Patient
    path("patients/appointments", PatientAppointments.as_view(), name="patient-appointments"),
]