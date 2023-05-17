from django.db import models

""" Creacion de la entidad Socio cuenta con:
nombre = nombre del Socio (tipo Str)
apellido = apellido del Socio (tipo Str)
fecha_nacimiento = la fecha de nacimiento del Socio (tipo Date)
activo = si el socio se encuentra activo o no (tipo Bool)
 """
class Socio(models.Model):
    nombre = models.CharField(max_length= 30)
    apellido = models.CharField(max_length= 30)
    fecha_nacimiento = models.DateField()
    activo = models.BooleanField(default= True)

    def __str__(self):
        return F"{self.apellido} {self.nombre}"
    
    class Meta:
        ordering = ['apellido', 'nombre', ]