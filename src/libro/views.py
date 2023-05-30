from django.shortcuts import redirect,get_object_or_404
from django.urls import reverse_lazy
from .models import Libro
# Create your views here.
def activar_libro(request, id):
    libro= get_object_or_404(Libro, id = id)
    libro.activo = True
    libro.save()
    
    return redirect(reverse_lazy('libro:ListarLibro'))