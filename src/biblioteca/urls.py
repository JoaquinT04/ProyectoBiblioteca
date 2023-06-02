from django.urls import path
from .views import CrearPrestamoLibro, desactivar_prestamo, ListarPrestamoLibro, EditarPrestamoLibro

app_name = 'prestamolibros'

urlpatterns = [
    path('nuevo/',CrearPrestamoLibro.as_view(), name= 'CrearPrestamoLibro' ),
    path('modificar/<int:pk>/',EditarPrestamoLibro.as_view(),name='EditarPrestamoLibro'),
    path('listar/',ListarPrestamoLibro.as_view(), name='ListarPrestamosLibro'),
    path('eliminar/<int:id>/',desactivar_prestamo, name='eliminar_prestamo'),
]

