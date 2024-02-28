from rest_framework import serializers
from core.serializers.slots import SlotSerializer
from bookings.models import *

class PatientSerializers(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = "__all__"

class AppointmentSerializers(serializers.ModelSerializer):
    patient = PatientSerializers(many=False, read_only=True)
    appointment_slot = SlotSerializer(many=False, read_only=True)
    class Meta:
        model = Appointments
        fields = "__all__"
        