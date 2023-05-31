from .models import PrestamoLibro
from django.views.generic import CreateView, ListView, UpdateView
from .forms import PrestamoLibroForm
from .models import PrestamoLibro
from django.urls import reverse_lazy

class ListarPrestamoLibro(ListView):
	model = PrestamoLibro
	template_name = "biblioteca/listar.html"

class CrearPrestamoLibro(CreateView):
    model = PrestamoLibro
    form_class = PrestamoLibroForm
    template_name = "biblioteca/crear.html"

class EditarPrestamoLibro(UpdateView):
    model = PrestamoLibro
    form_class = PrestamoLibroForm
    template_name = "biblioteca/editar.html"
    success_url = reverse_lazy('biblioteca:ListarPrestamoLibros') 