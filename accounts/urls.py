from django.urls import path
from accounts.views import *

urlpatterns = [
    path("register", RegisterAPI.as_view(), name="register-api"),
    path("verify", VerificationAPI.as_view(), name="send-verification-api"),
    path("verify/<int:pk>", VerificationAPI.as_view(), name="verification-api"),
    path("login", LoginAPI.as_view(), name="login-api"),
]