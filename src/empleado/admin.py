from django.contrib import admin
from models import Empleado

# Register your models here.

class EmpleadoAdmin(admin.ModelAdmin):
	# Me mostrará una tabla con la siguiente forma:
	# apellido | nombre | numero_legajo | activo
	list_display = ['apellido', 'nombre', 'numero_legajo','activo']
	# agrega opciones de busqueda por nombre o apellido
	search_fields = ['nombre', 'apellido']
	# agrega un filtro por el campo 'activo'
	list_filter = ['activo']
	
admin.site.register(Empleado, EmpleadoAdmin)
