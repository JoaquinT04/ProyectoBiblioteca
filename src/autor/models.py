from django.db import models

# Create your models here.
class Autor(models.Model):
    """Modelo representacion de la entidad Autor"""
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=30)
    activo = models.BooleanField(default = True)