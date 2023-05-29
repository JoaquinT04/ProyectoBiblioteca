from django.urls import path
from .views import (
    EditarLibro,
)

app_name = 'libros'

urlpatterns = [
    path('modificar/<int:pk>/',EditarLibro.as_view(), name='EditarLibro'),
]

