from django.conf import settings
from django.core.mail import send_mail
from accounts.models import Accounts
from base.models import Patients
from doctors.models import Doctors
import random

def sendEmailVerification(request, email):
    subject = 'Email Verification'
    otp = random.randint(100000,999999)
    message = f'OTP for verify email is {otp}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email,]
    send_mail( subject, message, email_from, recipient_list )
    return otp

def create_patient(name, email):
    try:
        account = Accounts.objects.get(email=email)
        patient = Patients.objects.create(
            first_name=name.split()[0],
            account=account
            )
    except Accounts.DoesNotExist:
        pass
    
def create_doctor(name, email):
    try:
        account = Accounts.objects.get(email=email)
        doctor = Doctors.objects.create(
            name=name,
            account=account
        )
    except Accounts.DoesNotExist:
        pass