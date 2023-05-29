from django.forms import ModelForm
from .models import Socio
from django import forms


class SocioForm(ModelForm):
		nombre  = forms.CharField(min_length=3,max_length=50, validators=[nombreValidator])
		apellido = forms.CharField(min_length=3,max_length=50, validators=[nombreValidator])
		class Meta:
				model = Socio
				fields = ["apellido","nombre","fecha_nacimiento"]
		