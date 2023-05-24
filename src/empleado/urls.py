from django.urls import path
from .views import (
    CrearEmpleado,
    ListarEmpleados,
    EditarEmpleado,
    activar_empleado,
    desactivar_empleado
    )

app_name = 'empleados'

urlpatterns = [
    path('crear',CrearEmpleado.as_view(), name= 'CrearEmpleado' ),
    path('listar',ListarEmpleados.as_view(), name= 'ListarEmpleados' ),
    path('activar/<int:id>', activar_empleado, name= 'activar_empleado'),
    path('modificar/<int:pk>/',EditarEmpleado.as_view(), name='EditarEmpleado'),
    path('desactivar/<int:id>', desactivar_empleado, name= 'desactivar_empleado'),
]

