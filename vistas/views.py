from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from .models import *
# Create your views here.
def ingreso(request):

	if request.method == 'POST':
		form = LoginUsuarioForm(request.POST)
		
		#print("Entre en method")
		#print(form['username'].value())
		objeto = get_object_or_404(Usuario, pk=form['username'].value())
		if form['password'].value() == objeto.password:
			
			request.session['username'] = objeto.username
			if esMedico(objeto):
				return redirect('/vistas/principal')
			elif esProfesor(objeto):
				return redirect('/vistas/principalProfesor')
			elif esRepresentante(objeto):
				return redirect('/vistas/principalRepresentante')			
		
	else:
		form = LoginUsuarioForm()
		
	return render(request, 'vistas/login.html', {'form': form})

def registro(request):
	
	if request.method == 'POST':
		form = RegistroUsuarioForm(request.POST)
		
		if form.is_valid():
			#print(form['tipo'].value())
			form.save()
			usr = Usuario.objects.get(pk=form['username'].value())
			if form['tipo'].value() == 'medico':
				med = Medico(usuario=usr)
				med.save()
			elif form['tipo'].value() == 'profesor':
				prof = Profesor(usuario=usr)
				prof.save()
			elif form['tipo'].value() == 'representante':
				rep = Representante(usuario=usr)
				rep.save()
			
			return redirect('/vistas/login')
	else:
		form = RegistroUsuarioForm()
	return render(request, 'vistas/registro.html', {'form': form})

def principal(request):
	usuario = get_object_or_404(Medico, pk=request.session['username'])
	pacientes = usuario.pacientes.all()
	args = {'usuario': usuario}
	return render(request, 'vistas/principal.html', args)

def principalRepresentante(request):
	usuario = get_object_or_404(Representante, pk = request.session['username'])
	return render(request, 'vistas/principalRepresentante.html', {'usuario': usuario})

def principalProfesor(request):
	usuario = get_object_or_404(Profesor, pk=request.session['username'])
	return render(request, 'vistas/principalProfesor.html', {'usuario': usuario})

def home(request):
	return render(request, 'vistas/home.html', {})