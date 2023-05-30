from .models import PrestamoLibro
from django.views.generic import CreateView
from .forms import PrestamoLibroForm



class CrearPrestamoLibro(CreateView):
    model = PrestamoLibro
    form_class = PrestamoLibroForm
    template_name = "prestamolibros/crear.html"