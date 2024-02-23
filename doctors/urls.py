from django.urls import path
from doctors.views import *

urlpatterns = [
    path("schedules", ScheduleAPI.as_view(), name="schedules-api"),
]