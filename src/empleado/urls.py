from django.urls import path
from .views import (CrearEmpleado,ListarEmpleados)

app_name = 'empleados'

urlpatterns = [
    path('crear',CrearEmpleado.as_view(), name= 'CrearEmpleado' ),
    path('listar',ListarEmpleados.as_view(), name= 'ListarEmpleados' ),
]

