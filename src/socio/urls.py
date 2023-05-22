from django.urls import path
from .views import (
    desactivar_socio,
    )

app_name = 'socios'

urlpatterns = [
    path('desactivar/<int:id>/',desactivar_socio, name='desactivar_socio'),
    
]

