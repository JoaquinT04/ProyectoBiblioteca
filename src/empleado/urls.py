from django.urls import path
from .views import activar_empleado

app_name = 'empleados'

urlpatterns = [
    path('activar/<int:id>', activar_empleado, name= 'activar_empleado'),
]