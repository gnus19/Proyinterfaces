from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Medico(User):
	especialidad = models.CharField(max_length=80)

class Profesor(User):
	area = models.CharField(max_length=80)

class Paciente(models.Model):
	enfermedad = models.CharField(max_length=80)