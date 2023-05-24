from django.urls import path
from .views import CrearAutor

app_name = 'autores'

urlpatterns = [
    path('nuevo/',CrearAutor.as_view(), name= 'CrearAutor' ),
]
