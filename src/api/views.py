from django.http import JsonResponse
from libro.models import Libro
from socio.models import Socio

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
			'autor': libro.autor.apellido+", "+libro.autor.nombre
		})
	else:
		return JsonResponse({})

def listar_socios(request):
    socios = Socio.objects.all()
    socios_dict = [
        {
            'id': socio.pk,
            'nombre': socio.nombre,
            'apellido': socio.apellido,
	    	'fecha de nacimiento': socio.fecha_nacimiento,
		    'activo': socio.activo, 
        }
        for socio in socios
    ]
    return JsonResponse(socios_dict, safe=False)