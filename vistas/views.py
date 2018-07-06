from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import *
# Create your views here.
def login(request):
	return render(request, 'vistas/login.html', {})

def registro(request):
	form = RegistroUsuarioForm(request.POST)

	return render(request, 'vistas/registro.html', {'form': form})

def principal(request):
	return render(request, 'vistas/principal.html', {})

def home(request):
	return render(request, 'vistas/home.html', {})