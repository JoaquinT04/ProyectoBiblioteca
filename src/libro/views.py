from django.shortcuts import render
from .models import Libro
from .forms import LibroForm
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.
class CrearLibro(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = "libros/crear.html"
    success_url = reverse_lazy('libros:ListarLibros') 