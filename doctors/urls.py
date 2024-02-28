from django.urls import path
from doctors.views import *

urlpatterns = [
    path("schedules", ScheduleAPI.as_view(), name="schedules-api"),
    path("appointments", AppoinmentsAPI.as_view(), name="appointments-api"),
    path("appointments/<int:pk>", AppoinmentsAPI.as_view(), name="appointment-api"),
    path("patients", PatientsAPI.as_view(), name="my-patients-api"),
    path("patients/<int:pk>", PatientsAPI.as_view(), name="patient-overview-api"),
    path("slots", MySlots.as_view(), name="my-slots-api"),
]