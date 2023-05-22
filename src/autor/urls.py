from django.urls import path
from .views import (
    EditarAutor,
    )

app_name = 'autores'

urlpatterns = [
    path('modificar/<int:id>/',EditarAutor.as_view(), name='EditarAutor'),
    
]

