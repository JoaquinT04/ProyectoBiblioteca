from django.urls import path
from .views import (
    EditarLibro,
    ListarLibro,
)

app_name = 'libros'

urlpatterns = [
    path('modificar/<int:pk>/',EditarLibro.as_view(), name='EditarLibro'),
    path('listado/',ListarLibro.as_view(), name= 'ListarLibros' ),
]

