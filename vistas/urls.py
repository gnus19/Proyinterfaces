# -*- coding: utf-8 -*-


from . import views
from django.conf.urls import url
from django.contrib.auth.views import login, logout

app_name = 'vistas'
urlpatterns = [
	url(r'^login/$', views.ingreso, name='ingreso'),
	url(r'^logout/$', views.ingreso, name='salir'),
	url(r'^registro/$', views.registro, name='registro'),
	url(r'^principalMedico/$', views.principalMedico, name='principalMedico'),
	url(r'^principalMedico/agregarPaciente/$', views.agregarPaciente, name='agregarPaciente'),
	url(r'^principalProfesor/agregarAlumno/$', views.agregarAlumno, name='agregarAlumno'),
	url(r'^principalRepresentante/$', views.principalRepresentante, name='principalRepresentante'),
	url(r'^principalProfesor/$', views.principalProfesor, name='principalProfesor'),
	url(r'^home/$', views.home, name='home'),
	url(r'^perfilProfesor/$', views.perfilProfesor, name = 'perfilProfesor'),
	url(r'^perfilMedico/$', views.perfilMedico, name = 'perfilMedico'),
	url(r'^perfilRepresentante/$', views.perfilRepresentante, name = 'perfilRepresentante')
]