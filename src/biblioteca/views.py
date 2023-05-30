from .models import PrestamoLibro
from django.views.generic import CreateView
from .forms import PrestamoLibroForm
from .models import PrestamoLibro
class ListarPrestamoLibro(ListView):
	model = PrestamoLibro
	template_name = "prestamoLibro/listar.html"

class CrearPrestamoLibro(CreateView):
    model = PrestamoLibro
    form_class = PrestamoLibroForm
    template_name = "prestamolibros/crear.html"