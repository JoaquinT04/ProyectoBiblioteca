from django.contrib import admin
from django.urls import path, include
from .views import listar_libros, detalle_libro, listar_socios

app_name = "api"

urlpatterns = [
	path('libros/<int:id>',detalle_libro,name = 'detalle_libro'),
    path('libros', listar_libros, name='listar_libros'),
    path('socios', listar_socios, name='listar_socios'),
]


