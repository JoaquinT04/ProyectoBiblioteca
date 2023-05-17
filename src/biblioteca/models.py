from django.db import models
from socio.models import Socio
from empleado.models import Empleado
from libro.models import Libro

# Create your models here.
class PrestamoLibro(models.Model):
    fecha_prestamos: models.DateField(auto_now_add=True)
    fecha_devolucion: models.DateField()
    socio: models.ForeignKey(Socio, on_delete=CASCADE)
    empleado: models.ForeignKey(Empleado, on_delete=CASCADE)
    libro: models.ForeignKey(Libro, on_delete=CASCADE)

#Generar el archivo migration (command makemigrations)

#Aplicar el archivo migration (command migrate)