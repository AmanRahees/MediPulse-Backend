from rest_framework.response import Response
from rest_framework.status import *
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.serializers import *
from accounts.func import *
from contexts.models import EmailVerification

# Create your views here.

class RegisterAPI(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        serializer = AccountRegisterSerializers(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            refresh['username'] = user.username
            refresh['role'] = user.role
            return Response({'refresh': str(refresh), 'access': str(refresh.access_token)}, status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)
    
class VerificationAPI(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email is required'}, status=HTTP_400_BAD_REQUEST)
        existing_verification = EmailVerification.objects.filter(email=email).first()
        if existing_verification:
            if existing_verification.is_verified:
                return Response({'error': 'Email is already registered'}, status=HTTP_400_BAD_REQUEST)
            else:
                otp = sendEmailVerification(request, email)
                if not otp:
                    return Response({'error': 'Failed to send verification email'}, status=HTTP_500_INTERNAL_SERVER_ERROR)
                existing_verification.otp = otp
                existing_verification.save()
        else:
            otp = sendEmailVerification(request, email)
            if not otp:
                return Response({'error': 'Failed to send verification email'}, status=HTTP_500_INTERNAL_SERVER_ERROR)
            existing_verification = EmailVerification.objects.create(email=email, otp=otp)
        return Response({'obj': existing_verification.id, 'message': 'Please check your Email to verify your Account'}, status=HTTP_200_OK)
    
    def put(self, request, pk):
        try:
            otp = request.data.get('otp')
            if not otp:
                return Response({'error': 'OTP is required'}, status=HTTP_400_BAD_REQUEST)
            obj = EmailVerification.objects.get(pk=pk)
            if obj.otp == otp:
                obj.is_verified = True
                obj.save()
                return Response({'message': 'verified'}, status=HTTP_202_ACCEPTED)
            else:
                return Response({'error': 'Invalid OTP'}, status=HTTP_400_BAD_REQUEST)
        except:
            return Response({'error': 'Email verification object not found'}, status=HTTP_400_BAD_REQUEST)
            
class LoginAPI(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = AccountLoginSerializers

class TokenRefreshAPI(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        refresh = request.data.get("refresh")
        if refresh:
            try:
                refresh_obj = RefreshToken(refresh)
                access_token = str(refresh_obj.access_token)
                return Response({'refresh': str(refresh), "access": access_token}, status=HTTP_200_OK)
            except:
                return Response({"Error": "Invalid Refresh Token."}, status=HTTP_400_BAD_REQUEST)
        else:
            return Response({"Error": "Refresh token not provided."}, status=HTTP_400_BAD_REQUEST)
