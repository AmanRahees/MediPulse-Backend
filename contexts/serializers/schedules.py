from rest_framework import serializers
from datetime import datetime
from contexts.serializers.utils import SchedulesSerializer
from doctors.models import Doctors
    
class DoctorScheduleSerializer(serializers.ModelSerializer):
    schedules = SchedulesSerializer(many=True)

    class Meta:
        model = Doctors
        fields = ["schedules"]

    def update(self, instance, validated_data):
        if 'schedules' in validated_data:
            instance.schedules.all().delete()
            schedules_data = self.validated_data['schedules']
            for schedule_data in schedules_data:
                schedule_data['slot_duration'] = instance.slot_duration
                instance.schedules.create(**schedule_data)
        instance.save()
        return instance
    