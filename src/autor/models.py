from django.db import models
from .validators import nombreValidator

# Create your models here.
class Autor(models.Model):
    """Modelo representacion de la entidad Autor"""
    nombre = models.CharField(max_length=50, validators=[nombreValidator])
    apellido = models.CharField(max_length=50, validators=[nombreValidator])
    nacionalidad = models.CharField(max_length=30, validators=[nombreValidator])
    activo = models.BooleanField(default = True)

    class Meta():
        ordering = ["apellido","nombre","nacionalidad"]
    
    def __str__(self):
        return f"{self.apellido},{self.nombre} ({self.nacionalidad})"