from rest_framework import serializers
from core.serializers.slots import SlotSerializer, DoctorSerializer
from bookings.models import *

class AppointmentSerializers(serializers.ModelSerializer):
    doctor = DoctorSerializer(many=False)
    appointment_slot = SlotSerializer(many=False)
    class Meta:
        model = Appointments
        fields = "__all__"