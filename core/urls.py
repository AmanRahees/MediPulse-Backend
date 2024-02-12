from django.urls import path
from core.views import *

urlpatterns = [
    path("login", LoginAPI.as_view(), name="admin-login-api"),
]