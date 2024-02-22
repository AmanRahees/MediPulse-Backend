from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from core.serializers.doctors import *

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
    pagination_class = PageNumberPagination