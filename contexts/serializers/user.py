from rest_framework import serializers
from accounts.models import Accounts
from base.models import Patients
from doctors.models import Doctors

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = "__all__"

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctors
        fields = "__all__"