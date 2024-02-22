from django.urls import path
from contexts.views import *

urlpatterns = [
    # user context
    path("patientInfo/<int:pk>", PatientInfoContext.as_view(), name="patient-info-context"),
    path("doctorInfo/<int:pk>", DoctorInfoContext.as_view(), name="doctor-info-context"),

    #wallet context
    path("wallet", WalletContext.as_view(), name="wallet-context"),
]