from django.urls import path
from .views import (
    ListarAutores,
    EditarAutor,
    )

app_name = 'autores'

urlpatterns = [
    path('listar/',ListarAutores.as_view(), name='EditarAutor'),
    path('modificar/<int:pk>/',EditarAutor.as_view(), name='EditarAutor'),  
]