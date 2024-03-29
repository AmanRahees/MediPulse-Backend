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
            refresh['email'] = user.email
            refresh['role'] = user.role
            return Response({'refresh': str(refresh), 'access': str(refresh.access_token)}, status=HTTP_201_CREATED)
        return Response(status=HTTP_400_BAD_REQUEST)
    
class VerificationAPI(APIView):
    def post(self, request):
        email = request.data.get('email')
        if not email:
            return Response({'error': 'Email is required'}, status=HTTP_400_BAD_REQUEST)
        if Accounts.objects.filter(email=email).exists():
            return Response({'error': 'Email is already Registered'}, status=HTTP_409_CONFLICT)
        else:
            existing_verification = EmailVerification.objects.filter(email=email).first()
            if existing_verification:
                if existing_verification.is_verified:
                    return Response({'message': 'Email is already Verified'}, status=HTTP_208_ALREADY_REPORTED)
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
        except EmailVerification.DoesNotExist:
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

class ForgotPasswordAPI(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:            
            email = request.data.get('email')
            if not email:
                return Response({'error': 'Email is required'}, status=HTTP_400_BAD_REQUEST)
            obj = EmailVerification.objects.get(email=email, is_verified=True)
            otp = sendEmailVerification(request, email)
            if not otp:
                return Response({'error': 'Failed to send verification email'}, status=HTTP_500_INTERNAL_SERVER_ERROR)
            obj.otp = otp
            obj.save()
            return Response({'message': 'Account verification has been sent to your email'}, status=HTTP_200_OK)
        except EmailVerification.DoesNotExist:
            return Response({'error': 'Account with this email does not exist'}, status=HTTP_400_BAD_REQUEST)

    def put(self, request):
        try:
            email = request.data.get('email')
            otp = request.data.get('otp')
            obj = EmailVerification.objects.get(email=email, is_verified=True)
            if obj.otp == otp:
                return Response({'message': 'verified'}, status=HTTP_200_OK)
            return Response({'error': 'Invalid OTP!'}, status=HTTP_200_OK)
        except:
            return Response({'error': 'Account with this email does not exist'}, status=HTTP_400_BAD_REQUEST)
        
class ResetPasswordAPI(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')
            confirm_password = request.data.get('confirm_password')
            if password == confirm_password:
                account = Accounts.objects.get(email=email)
                account.set_password(password)
                account.save()
                return Response({'message': 'Password Updated!'}, status=HTTP_202_ACCEPTED)
            return Response({'error': 'Passwords do not Match!'}, status=HTTP_400_BAD_REQUEST)
        except Accounts.DoesNotExist:
            return Response({'error': 'Account with this email does not exist'}, status=HTTP_400_BAD_REQUEST)
