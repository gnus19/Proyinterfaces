from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import *
# Create your views here.
def ingreso(request):

	if request.method == 'POST':
		form = LoginUsuarioForm(request.POST)
		
		#print("Entre en method")
		#print(form['username'].value())
		objeto = get_object_or_404(Usuario, pk=form['username'].value())
		request.session['username'] = objeto.username
		#print(request.session['username'])
		#print(objeto.password)
		return redirect('/vistas/principal')
		
	else:
		form = LoginUsuarioForm()
		
	return render(request, 'vistas/login.html', {'form': form})

def registro(request):
	
	if request.method == 'POST':
		form = RegistroUsuarioForm(request.POST)
		
		if form.is_valid():
			
			form.save()
			return redirect('/vistas/login')
	else:
		form = RegistroUsuarioForm()
	return render(request, 'vistas/registro.html', {'form': form})

def principal(request):
	return render(request, 'vistas/principal.html', {})

def home(request):
	return render(request, 'vistas/home.html', {})