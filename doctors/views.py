from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from doctors.permissions import isDoctor
from contexts.serializers.schedules import *
from doctors.serializers.appointments import *

# Create your views here.

class ScheduleAPI(APIView):
    permission_classes = [isDoctor]
    def post(self, request):
        doctor = get_object_or_404(Doctors, account=request.user)
        serializer = DoctorScheduleSerializer(doctor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.data, status=HTTP_400_BAD_REQUEST)
    
class AppoinmentsAPI(APIView):
    permission_classes = [isDoctor]
    def get(self, request):
        appointments = Appointments.objects.filter(doctor__account=request.user.id)
        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(appointments, request)
        serializer = AppointmentSerializers(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
    
    def post(self, request, pk):
        print(request.data)
        appointments = get_object_or_404(Appointments, pk=pk)
        serializer = AppointmentSerializers(appointments, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        
class PatientsAPI(APIView):
    permission_classes = [isDoctor]
    def get(self, request, pk=None):
        if pk is None:
            appointments = Appointments.objects.filter(doctor__account=request.user.id)
            my_patients = appointments.values('patient').distinct()
            patients = Patients.objects.filter(id__in=my_patients)
            serializer =  PatientSerializers(patients, many=True)
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            patient = get_object_or_404(Patients, pk=pk)
            serializer =  PatientSerializers(patient, many=False)
            return Response(serializer.data, status=HTTP_200_OK)
        
class MySlots(APIView):
    permission_classes = [isDoctor]
    def get(self, request):
        request_date = request.query_params.get('date', None)
        if request_date:
            slot_instance = get_object_or_404(SlotInstance, doctor__account=request.user.id, date=request_date)
            slots = Slots.objects.filter(slot_instance=slot_instance)
            serializer = SlotSerializer(slots, many=True)
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(status=HTTP_400_BAD_REQUEST)
    
