from django.contrib import admin
from .models import *

# Register your models here.

class patientDataAdmin(admin.ModelAdmin):
    new_patient = ('name','age','brainImage')

admin.site.register(PatientData,patientDataAdmin)