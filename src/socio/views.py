from django.shortcuts import render
from .models import Socio
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import SocioForm

from django.shortcuts import render

# Create your views here.

class EditarSocio(UpdateView):
    model = Socio
    form_class = SocioForm
    template_name = "socios/editar.html"
