from django.forms import ModelForm
from .models import Libro


class LibroForm(ModelForm):
		
		class Meta:
				model = Libro
				fields = ["titulo","descripcion","isbn","autor"]

class LibroForm(ModelForm):
		class Meta:
				model = Libro
				fields = '__all__'