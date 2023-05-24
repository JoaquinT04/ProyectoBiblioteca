from django.db import models

# Create your models here.
class Autor(models.Model):
    """Modelo representacion de la entidad Autor"""
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=30)
    activo = models.BooleanField(default = True)

    class Meta():
        ordering = ["apellido","nombre"]
    
    def __str__(self):
        return f"""nombre: {self.nombre} 
                   apellido: {self.apellido}
                   nacionalidad: {self.nacionalidad}
                   activo: {self.activo}"""