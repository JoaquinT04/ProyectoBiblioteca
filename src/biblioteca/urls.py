from django.urls import path
from .views import CrearPrestamoLibro

app_name = 'prestamolibros'

urlpatterns = [
    path('nuevo/',CrearPrestamoLibro.as_view(), name= 'CrearPrestamoLibro' ), 
]

