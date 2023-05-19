from django.urls import path
from .views import (CrearEmpleado,)

app_name = 'empleados'

urlpatterns = [
    path('crear',CrearEmpleado.as_view(), name= 'CrearEmpleado' ),
]