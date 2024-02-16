from django.contrib import admin
from accounts.models import Accounts
from base.models import *
from doctors.models import *
from bookings.models import *
from contexts.models import *

# Register your models here.

admin.site.register(Accounts)
admin.site.register(Patients)
admin.site.register(Doctors)
admin.site.register(Speciality)
admin.site.register(Appointments)
admin.site.register(Wallet)
admin.site.register(Educations)
admin.site.register(Experiences)
admin.site.register(Awards)