from rest_framework import serializers
from doctors.models import Doctors, SlotInstance, Slots
from core.serializers.doctors import DoctorSerializer

class SlotInstanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = SlotInstance
        fields = "__all__"

class SlotSerializer(serializers.ModelSerializer):
    slot_instance = SlotInstanceSerializer(many=False)
    class Meta:
        model = Slots
        fields = "__all__"