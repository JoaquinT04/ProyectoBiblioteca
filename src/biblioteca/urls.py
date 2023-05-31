from django.urls import path
from .views import CrearPrestamoLibro, EditarPrestamoLibro

app_name = 'prestamolibros'

urlpatterns = [
    path('nuevo/', CrearPrestamoLibro.as_view(), name= 'CrearPrestamoLibro'),
    path('modificar/<int:pk>/', EditarPrestamoLibro.as_view(), name= 'EditarPrestamoLibro'),  
]

