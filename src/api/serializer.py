from rest_framework import serializers
from libro.models import Libro
from autor.models import Autor
from empleado.models import Empleado

class AutorGetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Autor
		fields = ('id','nombre','apellido','nacionalidad')


class LibroGetSerializer(serializers.ModelSerializer):
	autor = AutorGetSerializer() # autor serializado
	class Meta:
		model = Libro
		#le paso el autor serializado declarado arriba
		fields = ('id','titulo','descripcion','isbn','autor')
	
class EmpleadoGetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Empleado
		fields = ('nombre','apellido','numero_legajo')
