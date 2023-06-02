from django.shortcuts import render,get_object_or_404
from django.http import JsonResponse
from libro.models import Libro
# Create your views here.

def detalle_libro(request,id):
	try: 
		libro = Libro.objects.get(id = id)
	except:
		libro = None

	if libro != None:
		return JsonResponse({
			'id':libro.id,
			'titulo': libro.titulo,
			'descripcion': libro.descripcion,
			'autor': libro.autor.nombre
		})
	else:
		return JsonResponse({})
