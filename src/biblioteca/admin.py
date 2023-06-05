from django.contrib import admin
from .models import PrestamoLibro

# Se define el atributo ordering para ordenar por fecha de devolucion.
# Se define elatributo list_display para mostrar campos por columna. 
# Se agrega la búsqueda por socio, empleado y libro.

class PrestamoLibroAdmin(admin.ModelAdmin):
        ordering = ['fecha_devolucion']
        list_display = ['fecha_prestamos', 'fecha_devolucion', 'socio', 'empleado', 'libro','activo']
        search_fields = ['socio', 'empleado', 'libro']
        

admin.site.register(PrestamoLibro, PrestamoLibroAdmin)