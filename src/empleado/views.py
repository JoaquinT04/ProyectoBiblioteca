from django.shortcuts import render
from django.views.generic import CreateView,ListView
from .models import Empleado
from .forms import EmpleadoForm
# Create your views here.

class ListarEmpleados(ListView):
	pass
class CrearEmpleado(CreateView):
	model = Empleado
	form_class = EmpleadoForm
	template_name = "empleados/crear.html"