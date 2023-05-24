from django.shortcuts import get_object_or_404, render
from .models import Autor
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import AutorForm

# Create your views here.
class EditarAutor(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = "autores/editar.html"

class ListarAutores(ListView):
	model = Autor
	template_name = "autores/listar.html"


def desactivar_autor(request, id):
    autor = get_object_or_404(Autor, id=id)
    autor.activo = False
    autor.save()
    
    mensaje = f'Autor: {autor.apellido}, {autor.nombre}\n'
    mensaje += f'Nacionalidad: {autor.nacionalidad}\n'
    mensaje += f'DESACTIVADO con exito!!'

    return mensaje