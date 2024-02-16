from rest_framework import serializers
from contexts.models import *

class SchedulesSerializer(serializers.ModelSerializer):
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