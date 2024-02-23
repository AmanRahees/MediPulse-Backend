from rest_framework import serializers
from datetime import datetime
from doctors.models import Doctors
from contexts.models import Schedules

class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedules
        fields = "__all__"
    
class DoctorScheduleSerializer(serializers.ModelSerializer):
    schedules = ScheduleSerializer(many=True)

    class Meta:
        model = Doctors
        fields = ["schedules"]

    def update(self, instance, validated_data):
        instance.schedules.clear()
        schedules_data = self.initial_data['schedules']
        for schedule_data in schedules_data:
            schedule_data['slot_duration'] = instance.slot_duration
            if 'id' in schedule_data:
                schedule_id = schedule_data.pop('id')
                schedule = Schedules.objects.get(id=schedule_id)
                instance.schedules.add(schedule)
            else:
                schedule_data['start_time'] = datetime.strptime(schedule_data['start_time'], '%H:%M').time()
            instance.schedules.create(**schedule_data)
        instance.save()
        return instance
    