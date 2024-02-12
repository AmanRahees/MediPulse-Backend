from django.urls import path
from accounts.views import *

urlpatterns = [
    path("register", RegisterAPI.as_view(), name="register-api"),
    path("login", LoginAPI.as_view(), name="login-api"),
    path("verify", VerificationAPI.as_view(), name="send-verification-api"),
    path("verify/<int:pk>", VerificationAPI.as_view(), name="verification-api"),
    path("token/refresh", TokenRefreshAPI.as_view(), name="token-refresh-api"),
    path("forgot-password", ForgotPasswordAPI.as_view(), name="forgot-password-api"),
    path("reset-password", ResetPasswordAPI.as_view(), name="reset-password-api"),
]