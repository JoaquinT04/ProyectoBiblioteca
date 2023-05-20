from django.db import models
from django.urls import reverse

# Create your models here.

# Modelo para el empleado
class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    numero_legajo = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)

    class Meta:
        ordering = ["apellido","nombre"]
    
    def __str__(self):
        return f"""nombre: {self.nombre} 
                   apellido: {self.apellido}
                   numero de legajo: {self.numero_legajo}
                   activo: {self.activo}"""

    def get_absolute_url(self):
        return reverse("empleado-detail", kwargs={"pk": self.pk})
    