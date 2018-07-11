# -*- coding: utf-8 -*-


from . import views
from django.conf.urls import url
from django.contrib.auth.views import login, logout

app_name = 'vistas'
urlpatterns = [
	url(r'^login/$', views.ingreso, name='ingreso'),
	url(r'^logout/$', views.ingreso, name='salir'),
	url(r'^registro/$', views.registro, name='registro'),
	url(r'^infoNutricional/$', views.infoNutricional, name='infoNutricional'),
	url(r'^juegos/$', views.juegos, name='juegos'),
	url(r'^principalMedico/$', views.principalMedico, name='principalMedico'),
	url(r'^principalMedico/agregarPaciente/$', views.agregarPaciente, name='agregarPaciente'),
	url(r'^principalRepresentante/$', views.principalRepresentante, name='principalRepresentante'),
	url(r'^principalRepresentante/agregarCita$', views.agregarCita, name='agregarCita'),
	url(r'^principalRepresentante/agregarRepresentado/$', views.agregarRepresentado, name='agregarRepresentado'),
	url(r'^principalRepresentante/agregarRepresentado/(?P<ciPaciente>.+)/$', views.agregarARepresentante, name='agregarARepresentante'),
	url(r'^principalProfesor/$', views.principalProfesor, name='principalProfesor'),
	url(r'^principalProfesor/agregarAlumno/$', views.agregarAlumno, name='agregarAlumno'),
	url(r'^home/$', views.home, name='home'),
	url(r'^perfil/$', views.perfil, name = 'perfil'),
	url(r'^perfilPaciente/(?P<ciPaciente>.+)/$', views.perfilPaciente, name='perfilPaciente'),
	url(r'^listajuegos/$', views.listajuegos, name='listajuegos'),

]