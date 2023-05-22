from django.shortcuts import render, get_object_or_404
from .models import Autor
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import AutorForm

class EditarAutor(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = "autores/editar.html"

def activar_autor(request, id):
    autor = get_object_or_404(Autor, id=id)
    autor.activo = True
    autor.save()
    
    mensaje = f'Autor: {autor.apellido}, {autor.nombre}\n'
    mensaje += f'Nacionalidad: {autor.nacionalidad}\n'
    mensaje += f'ACTIVADO con exito!!'

    return mensaje