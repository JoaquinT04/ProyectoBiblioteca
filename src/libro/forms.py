from django.forms import ModelForm
from .models import Libro, Autor
from .validators import isbnValidator
from django import forms


class LibroForm(ModelForm):
		autor = forms.ModelChoiceField(queryset=Autor.objects.filter(activo=True))
		isbn = forms.IntegerField(validators=[isbnValidator])
		class Meta:
				model = Libro
				fields = ["titulo","descripcion","isbn","autor"]
