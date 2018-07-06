from django import forms
from .models import *


class RegistroUsuarioForm(forms.Form):
	
	class Meta:
		model = User
		fields = [
			'username',
			'first_name',
			'last_name',
			'email',
		]
		labels = {
			'username': 'Nombre de usuario',
			'first_name': 'Nombres',
			'last_name': 'Apellidos',
			'email': 'Correo electronico',
		}