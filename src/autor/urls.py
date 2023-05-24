from django.urls import path
from .views import (
    EditarAutor,
    activar_autor,
    desactivar_autor,
    ListarAutores,
    CrearAutor
    )

app_name = 'autores'

urlpatterns = [
    path('nuevo/',CrearAutor.as_view(), name= 'CrearAutor' ),    
    path('listar/',ListarAutores.as_view(), name='ListarAutores'),
    path('modificar/<int:pk>/',EditarAutor.as_view(), name='EditarAutor'),
    path('activar/<int:id>/',activar_autor, name='activar_autor'),
    path('desactivar/<int:id>/',desactivar_autor, name='desactivar_autor'),
]

