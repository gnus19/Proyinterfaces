from django.contrib import admin
from vistas.models import *

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Paciente)
admin.site.register(Medico)
admin.site.register(Profesor)
admin.site.register(Representante)
admin.site.register(Cita)
admin.site.register(Dieta)