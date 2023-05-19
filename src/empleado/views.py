from django.shortcuts import render
from django.views.generic import CreateView
from .models import Empleado
from .forms import EmpleadoForm
# Create your views here.

class CrearEmpleado(CreateView):
	model = Empleado
	form_class = EmpleadoForm
	template_name = "empleados/crear.html"