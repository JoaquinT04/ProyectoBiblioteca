from .models import PrestamoLibro
from django.views.generic import CreateView, ListView, UpdateView
from .forms import PrestamoLibroForm
from .models import PrestamoLibro
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy

class ListarPrestamoLibro(ListView):
	model = PrestamoLibro
	template_name = "biblioteca/listar.html"

class CrearPrestamoLibro(CreateView):
    model = PrestamoLibro
    form_class = PrestamoLibroForm
    template_name = "biblioteca/crear.html"
    success_url =  reverse_lazy('prestamolibros:ListarPrestamosLibro')

class EditarPrestamoLibro(UpdateView):
    model = PrestamoLibro
    form_class = PrestamoLibroForm
    template_name = "biblioteca/editar.html"
    success_url =  reverse_lazy('prestamolibros:ListarPrestamosLibro')     

def desactivar_prestamo(request, id):
    prestamo = get_object_or_404(PrestamoLibro, id=id)
    prestamo.activo = False
    prestamo.save()
    return redirect(reverse_lazy('prestamolibros:ListarPrestamosLibro'))


    