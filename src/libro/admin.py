from django.contrib import admin
from .models import Libro

# Register your models here.
admin.site.register(Libro)

class LibroAdmin(admin.ModelAdmin):
	# me mostrara una tabla que se separaran de la siguiente forma
	# titulo | descripcion | isbn | autor | activo
	list_display = ['titulo', 'descripcion', 'isbn', 'autor','activo']
	search_fields = ['titulo']
	# agrega un filtro por titulo
	list_filter = ['activo']
