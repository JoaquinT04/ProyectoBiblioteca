from django.contrib import admin
from .models import Autor
# Register your models here.
#admin.site.register(Autor)


class AutorAdmin(admin.ModelAdmin):
    """ Se define el atributo list_display 
        Se Agrega opciones de búsqueda por nombre o apellido (list_search = search_fields)
        Se agrega la opción de filtrado por el field activo y nacionalidad (list_filter) """
    
    list_display = ["nombre","apellido","nacionalidad","activo"]
    list_filter = ["activo", "nacionalidad"]
    search_fields = ['nombre', 'apellido']

admin.site.register(Autor, AutorAdmin) # Registrar el modelo en el archivo admin.py
