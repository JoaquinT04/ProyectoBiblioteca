from django.urls import path
from .views import (
	EditarSocio,
	CrearSocio,
	ListarSocios,
	activar_socio,
	desactivar_socio
	)

app_name = 'socios'

urlpatterns = [
	path('nuevo/', CrearSocio.as_view(), name= 'CrearSocio'),
	path('listar/', ListarSocios.as_view(), name= 'ListarSocios'),
	path('modificar/<int:pk>/', EditarSocio.as_view(), name='EditarSocio'),
	path('activar/<int:id>/', activar_socio, name= 'activar_socio'),
	path('desactivar/<int:id>/', desactivar_socio, name= 'desactivar_socio'),
]

