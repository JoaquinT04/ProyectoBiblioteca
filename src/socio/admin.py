from django.contrib import admin

from .models import Socio

class SocioAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellido', 'fecha_nacimiento', 'activo']
    search_fields = ['nombre', 'apellido']
    list_filter = ['activo']

admin.site.register(Socio, SocioAdmin)