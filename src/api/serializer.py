from rest_framework import serializers
from libro.models import Libro
from autor.models import Autor
from empleado.models import Empleado
from socio.models import Socio
class AutorGetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Autor
		fields = ('id','nombre','apellido','nacionalidad','activo')


class LibroGetSerializer(serializers.ModelSerializer):
	autor = AutorGetSerializer() # autor serializado
	class Meta:
		model = Libro
		#le paso el autor serializado declarado arriba
		fields = ('id','titulo','descripcion','isbn','autor','activo')
	
class EmpleadoGetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Empleado
		fields = ('id','nombre','apellido','numero_legajo','activo')

class SocioGetSerializer(serializers.ModelSerializer):
	class Meta:
		model = Socio
		fields = ('id','apellido','nombre','fecha_nacimiento','activo')