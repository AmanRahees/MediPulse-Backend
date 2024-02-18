from rest_framework import serializers
from accounts.models import Accounts
from base.models import Patients
from doctors.models import Doctors
from contexts.serializers.speciality import *
from contexts.serializers.utils import *
from contexts.formats import format_nested_data

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patients
        fields = "__all__"

class DoctorSerializer(serializers.ModelSerializer):
    clinic_images = ClinicImgSerializer(many=True)
    schedules = SchedulesSerializer(many=True)
    education = EducationsSerializer(many=True)
    experience = ExperiencesSerializer(many=True)
    awards = AwardsSerializer(many=True)
    speciality = serializers.SerializerMethodField()

    class Meta:
        model = Doctors
        fields = "__all__"

    def get_speciality(self, instance):
        if instance.speciality:
            speciality = Speciality.objects.get(id=instance.speciality.id)
            serializer = SpecialitySerializer(speciality, many=False)
            return serializer.data

    def to_internal_value(self, data):
        if 'picture' in data and isinstance(data['picture'], str):
            data.pop('picture')
        clinic_images = format_nested_data(data, field_prefix="clinic_images")
        if clinic_images != []:
            data['clinic_images'] = clinic_images
        schedules = format_nested_data(data, field_prefix="schedules")
        if schedules != []:
            data['schedules'] = schedules
        educations = format_nested_data(data, field_prefix="education")
        if educations != []:
            data['education'] = educations
        experience = format_nested_data(data, field_prefix="experience")
        if experience != []:
            data['experience'] = experience
        awards = format_nested_data(data, field_prefix="awards")
        if awards != []:
            data['awards'] = awards
        return super().to_internal_value(data)

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

        if 'clinic_images' in validated_data:
            instance.clinic_images.clear()
            clinic_images_data = self.initial_data['clinic_images']
            for image_data in clinic_images_data:
                if 'id' in image_data:
                    clinic_image_id = image_data.pop('id')
                    clinic_image = ClinicImages.objects.get(id=clinic_image_id)
                    instance.clinic_images.add(clinic_image)
                else:
                    instance.clinic_images.create(**image_data)

        if 'schedules' in validated_data:
            instance.schedules.all().delete()
            schedules_data = self.initial_data['schedules']
            for schedule_data in schedules_data:
                instance.schedules.create(**schedule_data)

        if 'education' in validated_data:
            instance.education.all().delete()
            education_data = self.initial_data['education']
            for education_item in education_data:
                instance.education.create(**education_item)

        if 'experience' in validated_data:
            instance.experience.all().delete()
            experience_data = self.initial_data['experience']
            for experience_item in experience_data:
                instance.experience.create(**experience_item)

        if 'awards' in validated_data:
            instance.awards.all().delete()
            awards_data = self.initial_data['awards']
            for award_item in awards_data:
                instance.awards.create(**award_item)

        instance.save()
        return instance