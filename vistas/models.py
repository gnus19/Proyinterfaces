from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
import datetime, hashlib

# Create your models here.
class Usuario(models.Model):
    username    = models.EmailField(max_length=50, primary_key=True)
    password    = models.CharField(max_length=64, null=False)
    nombres     = models.CharField(max_length=80)
    apellidos   = models.CharField(max_length=80)

    def crearUsuario(self,usr,pwd):

        try:
            self.username = usr
            m = hashlib.sha256()
            p = str.encode(pwd)
            m.update(p)
            self.password = m.hexdigest()
            self.save()
            return True
        except:
            return False

    # Extrae por defecto el nombre de usuario
    def __str__(self):
        return self.username

    class Meta:
        app_label = 'vistas'

class Paciente(models.Model):
	nombres = models.CharField(max_length=80)
	apellidos = models.CharField(max_length=80)
	ci = models.CharField(max_length=9, primary_key=True)
	nacimiento = models.DateField()
	enfermedad = models.CharField(max_length=80)

class Medico(models.Model):
	usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
	especialidad = models.CharField(max_length=80)
	pacientes = models.ManyToManyField(Paciente, blank=True)

class Profesor(models.Model):
	usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True)
	area = models.CharField(max_length=80)
	alumnos = models.ManyToManyField(Paciente, blank=True)


