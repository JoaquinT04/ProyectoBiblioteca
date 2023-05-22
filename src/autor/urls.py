from django.urls import path
from .views import (
    EditarAutor,
    desactivar_autor,
    )

app_name = 'autores'

urlpatterns = [
    path('modificar/<int:id>/',EditarAutor.as_view(), name='EditarAutor'),
    path('desactivar/<int:id>/',desactivar_autor, name='desactivar_autor'),
]

