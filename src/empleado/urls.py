from django.urls import path
from .views import (CrearEmpleado,ListarEmpleados,activar_empleado)

app_name = 'empleados'

urlpatterns = [
    path('crear',CrearEmpleado.as_view(), name= 'CrearEmpleado' ),
    path('listar',ListarEmpleados.as_view(), name= 'ListarEmpleados' ),
    path('activar/<int:id>', activar_empleado, name= 'activar_empleado')
]

