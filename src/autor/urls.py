from django.urls import path
from .views import (
    EditarAutor,
    activar_autor,
    CrearAutor
    )

app_name = 'autores'

urlpatterns = [
    path('modificar/<int:id>/',EditarAutor.as_view(), name='EditarAutor'),
    path('activar/<int:id>/',activar_autor, name='activar_autor'),
    path('nuevo/',CrearAutor.as_view(), name= 'CrearAutor' ),    
]


