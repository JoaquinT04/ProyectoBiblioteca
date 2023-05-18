from django.shortcuts import render
from .models import Empleado
from .forms import EmpleadoForm
from django.views.generic import UpdateView, ListView

class EditarEmpleados(UpdateView):
    model = Empleado
    form_class = EmpleadoForm

class ListarEmpleados(ListView):
    model = Empleado
    template_name = "/empleado/listar.html"
