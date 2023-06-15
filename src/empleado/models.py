from django.db import models
from django.urls import reverse
from .validators import nombreValidator
# Create your models here.

# Modelo para el empleado
class Empleado(models.Model):
    nombre = models.CharField(max_length=30,validators=[nombreValidator])
    apellido = models.CharField(max_length=30,validators=[nombreValidator])
    numero_legajo = models.PositiveIntegerField(unique = True)
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ["apellido","nombre","numero_legajo"]
    
    def __str__(self):
        return f"{self.nombre},{self.apellido} ({self.numero_legajo})"

    def get_absolute_url(self):
        return reverse("empleados:ListarEmpleados")
    
