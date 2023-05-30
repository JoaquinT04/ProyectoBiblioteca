from django.shortcuts import render
from .models import PrestamoLibro
# Create your views here.
class ListarPrestamoLibro(ListView):
	model = PrestamoLibro
	template_name = "prestamoLibro/listar.html"
