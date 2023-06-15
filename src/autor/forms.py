from django.forms import ModelForm
from .models import Autor
from django import forms
from .validators import nombreValidator

class AutorForm(ModelForm):

		# Los 3 campos como maximo pueden tener 50 caracteres y como minimo 3 , con 
		# el validador propio de nombreValidator, valido que se ingresen caracteres
		# de la [a-z] o [A-Z] solamente
		nombre  = forms.CharField(min_length=3,max_length=50, validators=[nombreValidator], widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el nombre'}))
		apellido = forms.CharField(min_length=3,max_length=50, validators=[nombreValidator], widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el apellido'}))
		nacionalidad = forms.CharField(min_length=3,max_length=50, validators=[nombreValidator], widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese la nacionalidad'}))
		class Meta:
				model = Autor
				fields = ["apellido","nombre","nacionalidad"]