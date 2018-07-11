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
				return redirect('/vistas/principalMedico')
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
			if form['tipo'].value() == 'Medico':
				med = Medico(usuario=usr)
				med.save()
			elif form['tipo'].value() == 'Profesor':
				prof = Profesor(usuario=usr)
				prof.save()
			elif form['tipo'].value() == 'Representante':
				rep = Representante(usuario=usr)
				rep.save()
			
			return redirect('/vistas/login')
	else:
		form = RegistroUsuarioForm()
	return render(request, 'vistas/registro.html', {'form': form})


'''
Vistas del medico
'''
def principalMedico(request):
	usuario = get_object_or_404(Medico, pk=request.session['username'])
	citas = Cita.objects.filter(medico=usuario)
	args = {'usuario': usuario, 'citas': citas}
	return render(request, 'vistas/principalMedico.html', args)

def agregarPaciente(request):
	usuario = get_object_or_404(Medico, pk=request.session['username'])

	if request.method == 'POST':
		form = AgregarPacienteForm(request.POST)
		if form.is_valid():
			form.save()
			#Agregar a maedico#
			usuario = get_object_or_404(Medico, pk=request.session['username'])
			pacienteNuevo = Paciente.objects.get(pk=form['ci'].value())
			usuario.pacientes.add(pacienteNuevo)
			return redirect('/vistas/principalMedico')
	else:
		form = AgregarPacienteForm()
	args = {'usuario': usuario, 'form': form}
	return render(request, 'vistas/agregarPaciente.html', args)


'''
Vistas del representante
'''
def principalRepresentante(request):
	usuario = get_object_or_404(Representante, pk = request.session['username'])
	citas = Cita.objects.filter(representante=usuario)
	args = {'usuario': usuario, 'citas': citas}
	return render(request, 'vistas/principalRepresentante.html', args)

def agregarCita(request):
	usuario = get_object_or_404(Representante, pk=request.session['username'])

	if request.method == 'POST':
		form = AgregarCitaForm(request.POST)
		if form.is_valid():
			nuevaCita = form.save(commit=False)
			nuevaCita.representante = usuario
			nuevaCita.save()
			return redirect('/vistas/principalRepresentante')
		
	else:
		form = AgregarCitaForm()
	args = {'usuario': usuario, 'form': form}
	return render(request, 'vistas/agregarCita.html', args)

def agregarRepresentado(request):
	usuario = get_object_or_404(Representante, pk=request.session['username'])
	pacientes = Paciente.objects.all()

	args = {'usuario': usuario, 'pacientes': pacientes}
	return render(request, 'vistas/agregarRepresentado.html', args)

def agregarARepresentante(request, ciPaciente):
	usuario = get_object_or_404(Representante, pk=request.session['username'])

	nuevopaciente = Paciente.objects.get(pk=ciPaciente)
	usuario.representa.add(nuevopaciente)
	
	args = {'usuario': usuario}
	return redirect('/vistas/principalRepresentante')

'''
Vistas del profesor
'''
def principalProfesor(request):
	usuario = get_object_or_404(Profesor, pk=request.session['username'])
	args = {'usuario': usuario}
	return render(request, 'vistas/principalProfesor.html', args)

def agregarAlumno(request):
	usuario = get_object_or_404(Profesor, pk=request.session['username'])

	if request.method == 'POST':
		form = AgregarPacienteForm(request.POST)
		if form.is_valid():
			form.save()
			#Agregar a maedico#
			usuario = get_object_or_404(Profesor, pk=request.session['username'])
			pacienteNuevo = Paciente.objects.get(pk=form['ci'].value())
			usuario.pacientes.add(pacienteNuevo)
			return redirect('/vistas/principalProfesor')
	else:
		form = AgregarPacienteForm()
	args = {'usuario': usuario, 'form': form}
	return render(request, 'vistas/agregarPaciente.html', args)

def home(request):
	return render(request, 'vistas/home.html', {})

def perfil(request):
	
	return render(request, 'vistas/perfil.html', {})