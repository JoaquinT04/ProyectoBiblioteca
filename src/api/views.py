from django.http import JsonResponse
from libro.models import Libro

# Create your views here.
   
def listar_libros(request):
    libros = Libro.objects.all()
    libros_dict = [
        {
            'id': libro.id,
            'titulo': libro.titulo,
            'autor': str(libro.autor) 
        }
        for libro in libros
    ]
    return JsonResponse(libros_dict,safe=False)

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
