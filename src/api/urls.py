from django.contrib import admin
from django.urls import path, include
from .views import listar_libros

app_name = "api"

urlpatterns = [
    path('libros', listar_libros, name='listar_libros'),
]


