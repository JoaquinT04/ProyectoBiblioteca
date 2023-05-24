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
    success_url = reverse_lazy('socios:ListarSocioss') 

class ListarSocios(ListView):
    model = Socio
    template_name = "socios/listar.html"
    ordering = 'pk'
        
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
    
    """ mensaje = f'Socio: {socio.apellido}, {socio.nombre}\n'
    mensaje += f'Legajo: {socio.fecha_nacimiento}\n'
    mensaje += f'ACTIVADO con exito!!' """

    return redirect(reverse_lazy('socios:ListarSocios'))

def desactivar_socio(request, id):
    socio = get_object_or_404(Socio, id=id)
    socio.activo = False
    socio.save()
    
    """ mensaje = f'Socio: {socio.apellido}, {socio.nombre}\n'
    mensaje += f'Fecha de Nacimiento: {socio.fecha_nacimiento}\n'
    mensaje += f'ACTIVADO con exito!!' """
    return redirect(reverse_lazy('socios:ListarSocios'))
