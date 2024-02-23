from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from doctors.permissions import isDoctor
from contexts.serializers.schedules import *

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