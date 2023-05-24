from django.urls import path
from .views import (
    desactivar_socio,
		activar_socio,
		CrearSocio, 
		ListarSocio
    )

app_name = 'socios'

urlpatterns = [
    path('desactivar/<int:id>/',desactivar_socio, name='desactivar_socio'),
		path('nuevo/', CrearSocio.as_view(), name= 'CrearSocio' ),
    path('listar/', ListarSocio.as_view(), name= 'ListarSocios'),
		path('activar/<int:id>/', activar_socio, name='activar_socio'),
]

