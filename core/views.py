from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from core.serializers.specialities import *
from core.serializers.doctors import *

# Create your views here.

class LoginAPI(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            if user.is_superadmin == True:
                refresh = RefreshToken.for_user(user)
                refresh['username'] = user.username
                refresh['role'] = user.role
                return Response({'refresh': str(refresh), 'access': str(refresh.access_token)}, status=HTTP_200_OK)
            else:
                return Response({"Error": "Access Denied!"}, status=HTTP_403_FORBIDDEN)
        return Response({"Error": "Invalid Username or Password!"}, status=HTTP_400_BAD_REQUEST)
    
class SpecialityAPI(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request, pk=None):
        if pk:
            speciality = get_object_or_404(Speciality, pk=pk)
            serializer = SpecialitySerializer(speciality, many=False)
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            specialities = Speciality.objects.all()
            serializer = SpecialitySerializer(specialities, many=True)
            return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request):
        serializer = SpecialitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
        
    def put(self, request, pk):
        data = request.data.copy()
        speciality = get_object_or_404(Speciality, pk=pk)
        try:
            if type(data['speciality_image']) == str:
                data.pop('speciality_image')
        except:
            pass
        serializer = SpecialitySerializer(instance=speciality, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        speciality = get_object_or_404(Speciality, pk=pk)
        speciality.delete()
        return Response(status=HTTP_200_OK)
    
class DoctorsAPI(APIView):
    permission_classes = [IsAdminUser]
    def get(self, request, pk=None):
        if pk:
            doctor = get_object_or_404(Doctors, pk=pk)
            serializer = DoctorSerializer(doctor, many=False)
            return Response(serializer.data, status=HTTP_200_OK)
        else:
            doctors = Doctors.objects.all()
            serializer = DoctorSerializer(doctors, many=True)
            return Response(serializer.data, status=HTTP_200_OK)

    def post(self, request, pk):
        doctor = get_object_or_404(Doctors, pk=pk)
        doctor.is_approved = not doctor.is_approved
        doctor.save()
        serializer = DoctorSerializer(doctor, many=False)
        return Response(serializer.data, status=HTTP_200_OK)
    
#