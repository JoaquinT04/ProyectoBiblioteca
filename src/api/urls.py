from django.urls import path, include
#from .views import listar_libros, detalle_libro
""" urlpatterns = [
	path('libros/<int:id>',detalle_libro,name = 'detalle_libro'),
	path('libros', listar_libros, name='listar_libros'),
] """

# django rest framework
from .views import LibroViewSet,EmpleadoViewSet,AutorViewSet,SocioViewSet
from rest_framework import routers
app_name = "api"

router = routers.DefaultRouter()
router.register('libro', LibroViewSet)
router.register('empleado', EmpleadoViewSet)
router.register('autor', AutorViewSet)
router.register('socio', SocioViewSet)

urlpatterns = [
		path('',include(router.urls))
]



