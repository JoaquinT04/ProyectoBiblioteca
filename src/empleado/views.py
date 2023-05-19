from typing import Any, Dict
from django import http
from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Empleado
from .forms import EmpleadoForm
from django.views.generic import UpdateView, ListView,CreateView

class EditarEmpleado(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = "empleados/editar.html"
class ListarEmpleados(ListView):
	model = Empleado
	template_name = "empleados/listar.html"
class CrearEmpleado(CreateView):
	model = Empleado
	form_class = EmpleadoForm
	template_name = "empleados/crear.html"

# Create your views here.
def activar_empleado(request, pk):
    empleado= get_object_or_404(pk = pk)
    empleado.activo = True
    mensaje = "Empleado Activado"
    return mensaje

def desactivar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    empleado.activo = False
    empleado.save()
    
    mensaje = f'Empleado: {empleado.apellido}, {empleado.nombre}\n'
    mensaje += f'Legajo: {empleado.numero_legajo}\n'
    mensaje += f'DESACTIVADO con exito!!'

    return mensaje

