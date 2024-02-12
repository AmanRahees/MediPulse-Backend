from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

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