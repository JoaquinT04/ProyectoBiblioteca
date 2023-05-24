from django.urls import path
from .views import activar_socio

app_name = 'socios'

urlpatterns = [
	path('activar/<int:id>/', activar_socio, name='activar_socio'),
]