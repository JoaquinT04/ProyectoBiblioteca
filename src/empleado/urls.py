from django.urls import path
from .views import ListarEmpleados

app_name = 'empleados'

urlpatterns = [
    path('/empleados/listado',ListarEmpleados.as_view(), name= 'ListarEmpleados' ),
]
