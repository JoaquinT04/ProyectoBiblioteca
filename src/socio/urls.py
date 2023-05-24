from django.urls import path
from .views import CrearSocio, ListarSocio

app_name = 'socios'

urlpatterns = [
    path('nuevo/', CrearSocio.as_view(), name= 'CrearSocio' ),
    path('listar/', ListarSocio.as_view(), name= 'ListarSocios'),
]
