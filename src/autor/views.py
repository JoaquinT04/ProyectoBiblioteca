from django.shortcuts import get_object_or_404, render, redirect
from .models import Autor
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import AutorForm
from django.urls import reverse_lazy


class CrearAutor(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = "autores/crear.html"
    success_url =  reverse_lazy('autores:ListarAutores')     
class EditarAutor(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = "autores/editar.html"
    success_url =  reverse_lazy('autores:ListarAutores')     
    

class ListarAutores(ListView):
	model = Autor
	template_name = "autores/listar.html"

def desactivar_autor(request, id):
    autor = get_object_or_404(Autor, id=id)
    autor.activo = False
    autor.save()
    return redirect(reverse_lazy('autores:ListarAutores'))
    
def activar_autor(request, id):
    autor = get_object_or_404(Autor, id=id)
    autor.activo = True
    autor.save()
    return redirect(reverse_lazy('autores:ListarAutores'))
