from typing import Any, Dict
from django import http
from django.shortcuts import render
from .models import Empleado
from .forms import EmpleadoForm
from django.views.generic import UpdateView
from django.urls import reverse

# Create your views here.
class EditarEmpleado(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleado/crear.html'

    