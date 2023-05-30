from django.urls import path
from .views import (
    CrearLibro,
    )

app_name = 'libros'

urlpatterns = [
    path('nuevo/', CrearLibro.as_view(), name= 'CrearLibro' ),
]