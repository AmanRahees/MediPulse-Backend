from django.urls import path
from base.views import *

urlpatterns = [
    path("doctors", ListDoctors.as_view(), name="list-doctors"),
    path("doctors/<int:pk>", DoctorPreview.as_view(), name="preview-doctor"),
]