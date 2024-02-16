from rest_framework import serializers
from accounts.models import Accounts
from base.models import Patients
from doctors.models import Doctors
from contexts.serializers.utils import *

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = "__all__"

class DoctorSerializer(serializers.ModelSerializer):
    schedules = SchedulesSerializer(many=True)
    education = EducationsSerializer(many=True)
    experience = ExperiencesSerializer(many=True)
    awards = AwardsSerializer(many=True)

    class Meta:
        model = Doctors
        fields = "__all__"  

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.picture = validated_data.get('picture', instance.picture)
        instance.phone = validated_data.get('phone', instance.phone)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.consultation_fee = validated_data.get('consultation_fee', instance.consultation_fee)
        instance.services = validated_data.get('services', instance.services)
        instance.about = validated_data.get('about', instance.about)
        instance.location = validated_data.get('location', instance.location)
        instance.clinic_name = validated_data.get('clinic_name', instance.clinic_name)
        instance.clinic_address = validated_data.get('clinic_address', instance.clinic_address)
        instance.slot_duration = validated_data.get('slot_duration', instance.slot_duration)
        instance.is_approved = validated_data.get('is_approved', instance.is_approved)

        # Update the nested fields if present
        if 'schedules' in validated_data:
            instance.schedules.all().delete()
            schedules_data = validated_data.pop('schedules')
            for schedule_data in schedules_data:
                instance.schedules.create(**schedule_data)

        if 'education' in validated_data:
            instance.education.all().delete()
            education_data = validated_data.pop('education')
            for education_item in education_data:
                instance.education.create(**education_item)

        if 'experience' in validated_data:
            instance.experience.all().delete()
            experience_data = validated_data.pop('experience')
            for experience_item in experience_data:
                instance.experience.create(**experience_item)

        if 'awards' in validated_data:
            instance.awards.all().delete()
            awards_data = validated_data.pop('awards')
            for award_item in awards_data:
                instance.awards.create(**award_item)

        instance.save()
        return instance