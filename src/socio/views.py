from django.shortcuts import render
from .models import Socio
from .forms import SocioForm
from django.urls import reverse_lazy
from django.views.generic import CreateView , ListView

# Create your views here.
class ListarSocio(ListView):
    model = Socio
    template_name = "socios/listar.html"
    ordering = 'pk'

class CrearSocio(CreateView):
    model = Socio
    form_class = SocioForm
    template_name = "socios/crear.html"
    success_url = reverse_lazy('socios:ListarSocios') 
