from django.shortcuts import get_object_or_404
from .models import Libro

# Create your views here.

def desactivar_libro(request, id):
    libro= get_object_or_404(Libro, id = id)
    libro.activo = False
    libro.save()
    mensaje = "Libro Desactivado"
    return mensaje

