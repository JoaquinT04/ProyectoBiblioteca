from django.shortcuts import render
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

