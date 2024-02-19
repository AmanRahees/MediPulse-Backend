from rest_framework import serializers
from doctors.models import *

class DoctorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model =  Doctors
        fields = "__all__"