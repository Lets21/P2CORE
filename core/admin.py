from django.contrib import admin
from .models import Paciente, Doctor, Tratamiento, Cita

admin.site.register(Paciente)
admin.site.register(Doctor)
admin.site.register(Tratamiento)
admin.site.register(Cita)
