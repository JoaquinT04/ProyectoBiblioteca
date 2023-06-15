from django import forms
from django.forms import ModelForm
from .models import Empleado
from django import forms
from .validators import nombreValidator, positiveValidator
from django import forms
class EmpleadoForm(ModelForm):
	nombre  = forms.CharField(min_length=3,max_length=50, validators=[nombreValidator], widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el nombre'}))
	apellido = forms.CharField(min_length=3,max_length=50, validators=[nombreValidator], widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el apellido'}))
	numero_legajo = forms.IntegerField(validators=[positiveValidator], widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese n° de legajo'}))

	class Meta:
			model = Empleado
			fields = ["apellido","nombre","numero_legajo"]
