from django.core.exceptions import ValidationError
from .models import PrestamoLibro
from libro.models import Libro

def nombreValidator(value):
	# value va a tener todo el string que se introdujo en el input
	# voy a separar por cada espacio viendo si cada palabra tien o no 
	# un caracter numerico, caracter especial o palabras con tildes,
	#  si lo tiene tira un mensaje de error 
	if len(value)>=3:
		# value = "ja asbhe"
		for palabra in value.split(" "): #value.split(" ") me devuelve un array de palabras

			if not len(palabra)>=3:
				raise ValidationError("Debe ingresar más de 3 caracteres en cada palabra")

			if not palabra.isalpha():
				raise ValidationError("Debe ingresar solo letras")
			# isalpha() me devuelve True si el string contiene los caracteres
			# [a-z] o [A-Z] 
			# me devuelve False si el string contiene los caracteres
			# [0-9] o algun caracter especial como['#','.','-','á','é','í','ó','ú',etc] 
	else:	
		raise ValidationError("Debe ingresar más de 3 caracteres")
	

def validar_libro_disponible(value):
	prestamos = PrestamoLibro.objects.all()
	prestamo_dict = [
	    {
            'titulo': str(libro.libro.titulo),
	    	'activo': libro.activo
	    	
        }
        for libro in prestamos ]
    
	for libro in prestamo_dict:
		

		if libro["titulo"] == value.titulo and not libro["activo"] == False:
			raise ValidationError("El libro no esta disponible")
     

	

	
    
