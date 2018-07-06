from django.shortcuts import render, HttpResponse, get_object_or_404, redirect

# Create your views here.
def login_redirect(request):
	return redirect('/vistas/login/')