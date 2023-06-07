from django.urls import path
from .views import listar_libros, detalle_libro, listar_socios, listar_autores

app_name = "api"

urlpatterns = [
	path('libros/<int:id>',detalle_libro,name = 'detalle_libro'),
    path('libros', listar_libros, name= 'listar_libros'),
    path('socios', listar_socios, name='listar_socios'),
    path('autores', listar_autores, name= 'listar_autores'),
]


