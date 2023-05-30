from django.urls import path
from .views import (
    activar_libro,
)

app_name = 'libros'

urlpatterns = [
    path('activar/<int:id>/', activar_libro, name= 'activar_libro'),
]
