from django.db import models
from socio.models import Socio
from empleado.models import Empleado
from libro.models import Libro

# Create your models here.
class PrestamoLibro(models.Model):
    fecha_prestamos: models.DateField(auto_now_add= True)
    fecha_devolucion: models.DateField()
    socio: models.ForeignKey(Socio, on_delete= CASCADE)
    empleado: models.ForeignKey(Empleado, on_delete= CASCADE)
    libro: models.ForeignKey(Libro, on_delete= CASCADE)

    def __str__(self):
        cadena = f'Prestado Dia: {self.fecha_prestamos} - Devolucion Dia: {self.fecha_devolucion}\n'
        cadena += f'[Socio: {self.socio} - Libro: {self.libro}]\n'
        cadena += f'"Empleado: {self.empleado}"'
        return cadena