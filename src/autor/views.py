from django.shortcuts import render
from .models import Autor
from django.views.generic import UpdateView
from .forms import AutorForm

class EditarAutor(UpdateView):
    model = Autor
    form_class = AutorForm
    template_name = "autores/editar.html"