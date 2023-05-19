from django.db import models
from socio.models import Socio
from empleado.models import Empleado
from libro.models import Libro
from datetime import datetime

# El modelo PrestamoLibro llevara el registro de los libros prestados:
# fecha_prestado: Fecha que se presta. Se genera automaticamente.
# fecha_devolucion: Fecha de decolucion. Se debe cargar obligatoriamente.
# socio: Es la persona a quie se prestara el libro.
# empleado: Es la persona responsable del prestamo.
# libro: Libro que se presta.
class PrestamoLibro(models.Model):
    fecha_prestamos = models.DateField(auto_now_add= True)
    fecha_devolucion = models.DateField()
    socio = models.ForeignKey(Socio, on_delete= models.CASCADE)
    empleado = models.ForeignKey(Empleado, on_delete= models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete= models.CASCADE)

    def __str__(self):
        cadena = f'Prestado Dia: {self.fecha_prestamos.strftime("%d/%m/%Y")} - Devolucion Dia: {self.fecha_devolucion.strftime("%d/%m/%Y")}\n'
        cadena += f'[Socio: {self.socio} - Libro: {self.libro}]\n'
        cadena += f'"Empleado: {self.empleado}"'
        return cadena