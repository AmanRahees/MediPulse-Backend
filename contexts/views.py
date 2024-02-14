from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from contexts.serializers.user import *

# Create your views here.
    
class PatientInfoContext(APIView):
    def get(self, request, pk):
        patient = get_object_or_404(Patients, account=pk)
        serializer = PatientSerializer(patient, many=False)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def put(self, request, pk):
        patient = get_object_or_404(Patients, account=pk)
        serializer = PatientSerializer(patient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class DoctorInfoContext(APIView):
    def get(self, request, pk):
        doctor = get_object_or_404(Doctors, account=pk)
        serializer = DoctorSerializer(doctor, many=False)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def put(self, request, pk):
        doctor = get_object_or_404(Doctors, account=pk)
        serializer = DoctorSerializer(doctor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)