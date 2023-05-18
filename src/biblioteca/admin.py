from django.contrib import admin
from .models import PrestamoLibro

# Register your models here.
class PrestamoLibroAdmin(admin.ModelAdmin):
    ordering = ('fecha_devolucion')
    list_display = ('fecha_prestamos', 'fecha_devolucion', 'socio', 'empleado', 'libro')
    search_fields = ('socio', 'empleado', 'libro')

admin.site.register(PrestamoLibro, PrestamoLibroAdmin)