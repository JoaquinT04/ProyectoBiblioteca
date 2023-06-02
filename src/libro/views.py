from django.shortcuts import get_object_or_404 , redirect
from .models import Libro
from .forms import LibroForm
from django.views.generic import UpdateView, ListView, CreateView
from django.urls import reverse_lazy

class CrearLibro(CreateView):
    model = Libro
    form_class = LibroForm
    template_name = "libros/crear.html"
    success_url = reverse_lazy('libros:ListarLibros') 

class EditarLibro(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libros/editar.html' 
    success_url = reverse_lazy('libros:ListarLibros') 

class ListarLibros(ListView):
    model = Libro
    template_name = 'libros/listar.html'
    ordering = 'titulo'

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