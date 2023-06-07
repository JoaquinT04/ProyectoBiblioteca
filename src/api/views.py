from libro.models import Libro
from empleado.models import Empleado
from autor.models import Autor
from socio.models import Socio
# django rest framework
from rest_framework import viewsets
from .serializer import LibroGetSerializer,EmpleadoGetSerializer,AutorGetSerializer,SocioGetSerializer

# Create your views here.
class LibroViewSet(viewsets.ModelViewSet):
	queryset = Libro.objects.all()
	serializer_class = LibroGetSerializer

class EmpleadoViewSet(viewsets.ModelViewSet):
	queryset = Empleado.objects.all()
	serializer_class = EmpleadoGetSerializer

class AutorViewSet(viewsets.ModelViewSet):
	queryset = Autor.objects.all()
	serializer_class = AutorGetSerializer

class SocioViewSet(viewsets.ModelViewSet):
	queryset = Socio.objects.all()
	serializer_class = SocioGetSerializer