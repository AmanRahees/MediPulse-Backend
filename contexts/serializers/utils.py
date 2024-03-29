from rest_framework import serializers
from contexts.models import *

class ClinicImgSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClinicImages
        fields = "__all__"

class SchedulesSerializer(serializers.ModelSerializer):
    start_time = serializers.TimeField(format='%H:%M')
    end_time = serializers.TimeField(format='%H:%M', required=False, allow_null=True)
    class Meta:
        model = Schedules
        fields = "__all__"

class EducationsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Educations
        fields = "__all__"

class ExperiencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiences
        fields = "__all__"

class AwardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Awards
        fields = "__all__"