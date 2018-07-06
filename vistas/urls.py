# -*- coding: utf-8 -*-


from . import views
from django.conf.urls import url
from django.contrib.auth.views import login, logout

app_name = 'vistas'
urlpatterns = [
	url(r'^login/$', views.login, name='login'),
	url(r'^registro/$', views.registro, name='registro'),
	url(r'^principal/$', views.principal, name='principal'),
	url(r'^home/$', views.home, name='home')
]