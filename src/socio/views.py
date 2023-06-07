from django.shortcuts import redirect,get_object_or_404
from .models import Socio
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from .forms import SocioForm
from django.urls import reverse_lazy
# Create your views here.

class EditarSocio(UpdateView):
    model = Socio
    form_class = SocioForm
    template_name = "socios/editar.html"
    success_url = reverse_lazy('socios:ListarSocios') 

class ListarSocios(ListView):
    model = Socio
    template_name = "socios/listar.html"
    ordering = ("apellido", "nombre")
        
class CrearSocio(CreateView):
    model = Socio
    form_class = SocioForm
    template_name = "socios/crear.html"
    success_url = reverse_lazy('socios:ListarSocios') 

# Create your views here.
def activar_socio(request, id):
    socio = get_object_or_404(Socio, id=id)
    socio.activo = True
    socio.save()

    return redirect(reverse_lazy('socios:ListarSocios'))

def desactivar_socio(request, id):
    socio = get_object_or_404(Socio, id=id)
    socio.activo = False
    socio.save()
    return redirect(reverse_lazy('socios:ListarSocios'))
