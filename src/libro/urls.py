from django.urls import path
from .views import desactivar_libro
	

app_name = 'libros'

urlpatterns = [
	path('desactivar/<int:id>/', desactivar_libro, name= 'desactivar_libro'),
]