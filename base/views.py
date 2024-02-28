from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from doctors.permissions import isPatient
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from core.serializers.doctors import *
from core.serializers.slots import *
from base.serializers.appointments import Appointments, AppointmentSerializers
from doctors.func import get_day_of_week

# Create your views here.

class ListDoctors(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = DoctorSerializer
    queryset = Doctors.objects.exclude(is_approved=False)
    pagination_class = PageNumberPagination
    
class DoctorPreview(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = DoctorSerializer
    queryset = Doctors.objects.exclude(is_approved=False)

class ListSlots(generics.ListAPIView):
    permission_classes = [AllowAny]
    serializer_class = SlotSerializer
    queryset = Slots.objects.exclude(slot_instance__doctor__is_approved=False)

    def get_queryset(self):
        try:
            pk = self.kwargs['doctor_id']
            date = datetime.strptime(self.kwargs['date'], '%Y-%m-%d').date()
        except ValueError:
            return Slots.objects.none()
        doctor = get_object_or_404(Doctors, pk=pk)
        schedule = doctor.schedules.filter(day=get_day_of_week(date)).first()
        if schedule:
            isExists = SlotInstance.objects.filter(doctor=doctor, date=date).exists()
            if isExists:
                slot_instance = SlotInstance.objects.get(doctor=doctor, date=date)
            else:
                slot_instance = SlotInstance.objects.create(doctor=doctor, date=date)
            slots = Slots.objects.filter(slot_instance=slot_instance)
            return slots
        else:
            return Slots.objects.none()
        
class PatientAppointments(generics.ListAPIView):
    permission_classes = [isPatient]
    serializer_class = AppointmentSerializers
    pagination_class = PageNumberPagination
    
    def get_queryset(self):
        return Appointments.objects.filter(patient__account=self.request.user.id)

