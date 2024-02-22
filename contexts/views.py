from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.views import APIView
from rest_framework import generics
from contexts.serializers.user import *
from contexts.serializers.wallet import *

# Create your views here.
    
class PatientInfoContext(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        patient = get_object_or_404(Patients, account=pk)
        serializer = PatientSerializer(patient, many=False)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def put(self, request, pk):
        patient = get_object_or_404(Patients, pk=pk)
        serializer = PatientSerializer(patient, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class DoctorInfoContext(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        doctor = get_object_or_404(Doctors, account=pk)
        serializer = DoctorSerializer(doctor, many=False)
        return Response(serializer.data, status=HTTP_200_OK)
    
    def put(self, request, pk):
        data = request.data.copy()
        doctor = get_object_or_404(Doctors, pk=pk)
        if 'services[]' in data:
            services = data.getlist('services[]', [])
            if services:
                doctor.services.clear()
                for service in services:
                    doctor.services.append(service)
                doctor.save()
        serializer = DoctorSerializer(doctor, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
    
class WalletContext(generics.RetrieveAPIView):
    serializer_class = WalletSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return get_object_or_404(Wallet, account=self.request.user)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=HTTP_200_OK)
    
