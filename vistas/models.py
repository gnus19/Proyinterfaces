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

class Dieta(models.Model):
    paciente = models.OneToOneField(Paciente, on_delete=models.PROTECT)
    hora = models.CharField(max_length=80)
    porcion = models.CharField(max_length=80)
    alimento = models.CharField(max_length=80)

class Medico(models.Model):
	usuario = models.OneToOneField(Usuario, on_delete=models.PROTECT, primary_key=True)
	especialidad = models.CharField(max_length=80, blank=True)
	pacientes = models.ManyToManyField(Paciente, blank=True)


class Profesor(models.Model):
	usuario = models.OneToOneField(Usuario, on_delete=models.PROTECT, primary_key=True)
	area = models.CharField(max_length=80, blank=True)
	alumnos = models.ManyToManyField(Paciente, blank=True)

class Representante(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.PROTECT, primary_key=True)
    representa = models.ManyToManyField(Paciente, blank=True)

class Cita(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.PROTECT)
    representante = models.ForeignKey(Representante, on_delete=models.PROTECT)
    fecha = models.DateField()
    hora = models.CharField(max_length=6)

'''
Funciones auxiliares
'''

def esMedico(usr):
    try:
        med = Medico.objects.get(pk=usr)
        return True
    except:
        return False

def esProfesor(usr):
    try:
        prof = Profesor.objects.get(pk=usr)
        return True
    except:
        return False

def esRepresentante(usr):
    try:
        rep = Representante.objects.get(pk=usr)
        return True
    except:
        return False