from rest_framework import serializers
from accounts.serializers import AccountSerializer
from contexts.serializers.speciality import SpecialitySerializer
from contexts.serializers.utils import *
from doctors.models import *

class DoctorSerializer(serializers.ModelSerializer):
    account = AccountSerializer(many=False)
    speciality = SpecialitySerializer(many=False)
    earnings = serializers.SerializerMethodField()
    ratings = serializers.SerializerMethodField()
    clinic_images = ClinicImgSerializer(many=True)
    education = EducationsSerializer(many=True)
    experience = ExperiencesSerializer(many=True)
    awards = AwardsSerializer(many=True)

    class Meta:
        model =  Doctors
        fields = "__all__"

    def get_account(self, instance):
        account = Accounts.objects.get(id=instance.account.id)
        return account
    
    def get_earnings(self, instance):
        return 5000
    
    def get_ratings(self, instance):
        return 3.8