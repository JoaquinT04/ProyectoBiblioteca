from django.forms import ModelForm
from .models import Socio

class SocioForm(ModelForm):
		class Meta:
				model = Socio
				fields = ['nombre', 'apellido', 'fecha_nacimiento']
