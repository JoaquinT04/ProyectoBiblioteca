from django.contrib import admin
from django.urls import path, include
from .views import listar_libros, detalle_libro, listar_autores

app_name = "api"

urlpatterns = [
	path('libros/<int:id>',detalle_libro,name = 'detalle_libro'),
    path('libros', listar_libros, name= 'listar_libros'),
    path('autores', listar_autores, name= 'listar_autores'),
]


