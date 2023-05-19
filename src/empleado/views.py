from django.shortcuts import render
from .models import Empleado
from .forms import EmpleadoForm
from django.shortcuts import get_object_or_404

# Create your views here.

def activar_empleado(request, pk):
    empleado= get_object_or_404(pk = pk)
    empleado.activo = True
    mensaje = "Empleado Activado"
    return mensaje
