from django.forms import ModelForm
from .models import Autor
from django import forms
from .validators import nombreValidator

class AutorForm(ModelForm):

		# Los 3 campos como maximo pueden tener 50 caracteres y como minimo 3 , con 
		# el validador propio de nombreValidator, valido que se ingresen caracteres
		# de la [a-z] o [A-Z] solamente
		nombre  = forms.CharField(min_length=3,max_length=50, validators=[nombreValidator])
		apellido = forms.CharField(min_length=3,max_length=50, validators=[nombreValidator])
		nacionalidad = forms.CharField(min_length=3,max_length=50, validators=[nombreValidator])
		class Meta:
				model = Autor
				fields = ["apellido","nombre","nacionalidad"]
