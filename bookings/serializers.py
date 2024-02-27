from rest_framework import serializers
from bookings.models import *

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointments
        fields = "__all__"