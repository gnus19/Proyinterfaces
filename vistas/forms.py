from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *
import hashlib, datetime
import re

CHOICES = [('medico', 'medico'), ('profesor', 'profesor'), ('representante', 'representante')]

class RegistroUsuarioForm(forms.ModelForm):
	tipo = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
	
	class Meta:
		model = Usuario
		fields = [
			'username',
			'nombres',
			'apellidos',
			'password',
			
		]
		labels = {
			'username': 'Correo electronico',
			'nombres': 'Nombres',
			'apellidos': 'Apellidos',
			'password': 'Contrasena',
			
		}
		widgets = {
			'username': forms.EmailInput(attrs={'class':'input100', 'placeholder': 'Correo electronico'}),
			'nombres': forms.TextInput(attrs={'class':'input100', 'placeholder': 'Nombres'}),
			'apellidos': forms.TextInput(attrs={'class':'input100', 'placeholder': 'Apellidos'}),
			'password': forms.PasswordInput(attrs={'class':'input100', 'placeholder': 'Password', 'type': 'password'}),

		}


class LoginUsuarioForm(forms.Form):

	username = forms.EmailField(max_length=30, widget=forms.EmailInput(attrs={'class':'input100', 'placeholder': 'Correo electronico'}))
	password = forms.CharField(max_length=64, widget=forms.PasswordInput(attrs={'class':'input100', 'placeholder': 'Password', 'type': 'password'}))

	def clean(self):
		limpio = super(LoginUsuarioForm, self).clean()
		usr = limpio.get('username')
		pwd = limpio.get('password')
		try:
			q = Usuario.objects.get(pk=usr)
			m = hashlib.sha256()
			p = str.encode(pwd)
			m.update(p)

			if (m.hexdigest()==q.password):
				pass
				#self.usuario = q
			else:
				self.add_error('username', 'Usuario o clave incorrecto')
		except:
			self.add_error('username', 'Usuario o clave incorrecto')
		return limpio

	class Meta:
		model = Usuario

		exclude = [
			'nombres',
			'apellidos'
		]
		
class AgregarPacienteForm(forms.ModelForm):

	class Meta:
		model = Paciente

		exclude = []

		widgets = {
			'nombres': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombres'}),
			'apellidos': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Apellidos'}),
			'ci': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'C.I'}),
			'nacimiento': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Nacimiento'}),
			'enfermedad': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enfermedad'}),
		}
