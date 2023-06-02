from django.shortcuts import render
from django.http import JsonResponse
from libro.models import Libro


    
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