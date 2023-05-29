from django.shortcuts import get_object_or_404 , redirect
from .models import Libro
from .forms import LibroForm
from django.views.generic import UpdateView, ListView,CreateView
from django.urls import reverse_lazy

class EditarLibro(UpdateView):
    model = Libro
    form_class = LibroForm
    template_name = 'libros/editar.html' 
    success_url = reverse_lazy('libros:ListarLibros') 