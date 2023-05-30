from django.urls import path
from .views import (
    CrearLibro,
    EditarLibro,
    ListarLibro,
		desactivar_libro,
    activar_libro,
)

app_name = 'libros'

urlpatterns = [
    path('nuevo/', CrearLibro.as_view(), name= 'CrearLibro' ),
    path('modificar/<int:pk>/',EditarLibro.as_view(), name='EditarLibro'),
    path('listado/',ListarLibro.as_view(), name= 'ListarLibros' ),
    path('activar/<int:id>/', activar_libro, name= 'activar_libro'),
		path('desactivar/<int:id>/', desactivar_libro, name= 'desactivar_libro'),
]