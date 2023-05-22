from django.shortcuts import render, get_object_or_404
from .models import Socio
from django.views.generic import CreateView, ListView, UpdateView, DeleteView


def desactivar_socio(request, id):
    socio = get_object_or_404(Socio, id=id)
    socio.activo = False
    socio.save()
    
    mensaje = f'Socio: {socio.apellido}, {socio.nombre}\n'
    mensaje += f'Fecha de Nacimiento: {socio.fecha_nacimiento}\n'
    mensaje += f'ACTIVADO con exito!!'

    return mensaje