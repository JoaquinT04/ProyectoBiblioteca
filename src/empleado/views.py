from django.shortcuts import render
from .models import Empleado
from django.shortcuts import get_object_or_404

# Create your views here.
def desactivar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    empleado.activo = False
    empleado.save()
    
    mensaje = f'Empleado: {empleado.apellido}, {empleado.nombre}\n'
    mensaje += f'Legajo: {empleado.numero_legajo}\n'
    mensaje += f'DESACTIVADO con exito!!'

    return mensaje

