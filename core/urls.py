from django.urls import path
from core.views import *

urlpatterns = [
    path("login", LoginAPI.as_view(), name="admin-login-api"),
    path("speciality", SpecialityAPI.as_view(), name="specialities-api"),
    path("speciality/<int:pk>", SpecialityAPI.as_view(), name="speciality-api"),
    path("doctors", DoctorsAPI.as_view(), name="doctors-api"),
    path("doctors/<int:pk>", DoctorsAPI.as_view(), name="doctor-api"),
]