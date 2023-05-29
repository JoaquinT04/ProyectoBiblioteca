from django.forms import ModelForm
from .models import Socio
from django import forms


class SocioForm(ModelForm):
		nombre = forms.CharField()
		apellido = forms.CharField()
		class Meta:
				model = Socio
				fields = ['nombre', 'apellido', 'fecha_nacimiento']
		