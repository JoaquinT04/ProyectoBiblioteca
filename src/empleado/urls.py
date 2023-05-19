from django.urls import path
from .views import desactivar_empleado

app_name = 'empleados'

urlpatterns = [
    path('desactivar/<int:id>', desactivar_empleado, name= 'desactivar_empleado'),
]