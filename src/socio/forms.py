from django.forms import ModelForm
from .models import Socio
from django import forms
from .validators import nombreValidator


class SocioForm(ModelForm):
		nombre  = forms.CharField(min_length=3,max_length=50, validators=[nombreValidator], widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el nombre'}))
		apellido = forms.CharField(min_length=3,max_length=50, validators=[nombreValidator], widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el apellido'}))
		class Meta:
				model = Socio
				fields = ["apellido","nombre","fecha_nacimiento"]
				widgets = {
					'fecha_nacimiento' : forms.DateInput(attrs={'class':'form-control', 'placeholder':'dd/mm/aaaa'})
				}