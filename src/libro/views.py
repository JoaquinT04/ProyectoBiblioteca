from django.shortcuts import get_object_or_404, redirect
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

def desactivar_libro(request, id):
    libro= get_object_or_404(Libro, id = id)
    libro.activo = False
    libro.save()
    return redirect(reverse_lazy('libros:ListarLibros'))

def activar_libro(request, id):
    libro= get_object_or_404(Libro, id = id)
    libro.activo = True
    libro.save()
    return redirect(reverse_lazy('libros:ListarLibros'))