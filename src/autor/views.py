from django.shortcuts import render
from .models import Autor
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import AutorForm

# Create your views here.
class CrearAutor(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = "autores/crear.html"
    success_url = reverse_lazy('empleados:ListarEmpleados') 
