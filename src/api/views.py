from libro.models import Libro
from empleado.models import Empleado
# django rest framework
from rest_framework import viewsets
from .serializer import LibroGetSerializer,EmpleadoGetSerializer

# Create your views here.
class LibroViewSet(viewsets.ModelViewSet):
	queryset = Libro.objects.all()
	serializer_class = LibroGetSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
	queryset = Empleado.objects.all()
	serializer_class = EmpleadoGetSerializer