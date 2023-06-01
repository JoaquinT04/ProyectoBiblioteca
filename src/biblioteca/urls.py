from django.urls import path
from .views import CrearPrestamoLibro,ListarPrestamoLibro

app_name = 'prestamolibros'

urlpatterns = [
    path('nuevo/',CrearPrestamoLibro.as_view(), name= 'CrearPrestamoLibro' ),
    path('listar/',ListarPrestamoLibro.as_view(), name= 'ListarPrestamoLibro' ),
]

