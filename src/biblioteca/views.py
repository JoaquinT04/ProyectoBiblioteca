from .models import PrestamoLibro
from django.views.generic import CreateView,ListView
from .forms import PrestamoLibroForm
from .models import PrestamoLibro

class ListarPrestamoLibro(ListView):
	model = PrestamoLibro
	template_name = "prestamoLibros/listar.html"

class CrearPrestamoLibro(CreateView):
    model = PrestamoLibro
    form_class = PrestamoLibroForm
    template_name = "prestamolibros/crear.html"