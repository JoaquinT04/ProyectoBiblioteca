from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Empleado
from .forms import EmpleadoForm
from django.views.generic import UpdateView, ListView,CreateView

class EditarEmpleados(UpdateView):
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
