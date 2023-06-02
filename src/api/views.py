from django.shortcuts import render
from django.http import JsonResponse
from libro.models import Libro
from autor.models import Autor

"""def listar_libros(request):
    libros = Libro.objects.all()
    print (libros)
    data = []
    for libro in libros:
        data.append({
            'id': libro.id,
            'titulo': libro.titulo,
            'autor': libro.autor,
        })
    return JsonResponse(data, safe=False)"""


def listar_libros(request):
  
    libros = Libro.objects.values('id', 'titulo','autor')
    print(libros)
    data = {
        'libros' : list(libros)
    }
    return JsonResponse(data)