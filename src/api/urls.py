from django.contrib import admin
from django.urls import path, include
#from .views import listar_libros, detalle_libro
""" urlpatterns = [
	path('libros/<int:id>',detalle_libro,name = 'detalle_libro'),
	path('libros', listar_libros, name='listar_libros'),
] """

app_name = "api"

# django rest framework
from .views import LibroViewSet,EmpleadoViewSet
from rest_framework import routers
router = routers.DefaultRouter()
router.register('libro', LibroViewSet)
router.register('empleado', EmpleadoViewSet)

urlpatterns = [
		path('',include(router.urls))
]



