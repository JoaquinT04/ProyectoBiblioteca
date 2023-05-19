from django.db import models
from autor.models import Autor
# Create your models here.
class Libro(models.Model):
    # Titulo del libro (maximo 30 caracteres)
    titulo = models.CharField(max_length=30)
    # descripción del libro (cabe la posibilidad de no tener descripcion) y tambien se acepta no poner descripcion 
    descripcion = models.TextField(blank=True,null=True)
    # isbn del libro (El isbn es un estandard número de 13 cifras que identifica a cada libro en el mundo)
    isbn = models.PositiveIntegerField()
    # aqui estara la información del autor que se encuentra en su respectivo modelo
    autor =  models.ForeignKey(Autor, on_delete= models.CASCADE)
    # activo hara referencia asi el libro esta disponible o no, por defecto a la hora de que se cree un libro estara disponible
    activo: models.BooleanField(default=True)

    def __str__(self) -> str:
      return f"""titulo: {self.titulo}
                 descripcion: {self.descripcion}
                 isbn: {self.isbn}
                 autor: {self.autor}
                 """
    class Meta:
      ordering = [
        "titulo",
        "isbn"
      ]