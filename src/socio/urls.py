from django.urls import path
from .views import (EditarSocio)

app_name = 'socios'

urlpatterns = [
	path('modificar/<int:id>/',EditarSocio.as_view(), name='EditarSocio'),
]

