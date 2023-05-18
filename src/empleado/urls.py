from django.urls import path
from .views import ListarEmpleados

app_name = 'empleado'

urlpatterns = [
    path('/empleados/listado',ListarEmpleados.as_view(), name= 'Listado de Empleados' ),
]
