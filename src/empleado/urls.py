from django.urls import path
from .views import EditarEmpleado

app_name = 'empleados'

urlpatterns = [
    path('modificar/<int:id>/',EditarEmpleado.as_view(), name='EditarEmpleado'),
]
