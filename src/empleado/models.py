from django.db import models

# Create your models here.

# Modelo para el empleado
class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    numero_legajo = models.PositiveIntegerField()
    activo = models.BooleanField(default=True)