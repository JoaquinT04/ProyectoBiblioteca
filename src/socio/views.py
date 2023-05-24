from django.shortcuts import render, get_object_or_404
from socio.models import Socio

# Create your views here.
def activar_socio(request, id):
    socio = get_object_or_404(Socio, id=id)
    socio.activo = True
    socio.save()
    
    mensaje = f'Socio: {socio.apellido}, {socio.nombre}\n'
    mensaje += f'Legajo: {socio.fecha_nacimiento}\n'
    mensaje += f'ACTIVADO con exito!!'

    return mensaje
