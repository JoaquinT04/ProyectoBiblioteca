from django import forms
from django.forms import ModelForm
from .models import Empleado
from django import forms
from .validators import nombreValidator
from django import forms
class EmpleadoForm(ModelForm):
	nombre  = forms.CharField(min_length=3,max_length=50, validators=[nombreValidator])
	apellido = forms.CharField(min_length=3,max_length=50, validators=[nombreValidator])
	class Meta:
			model = Empleado
			fields = ["apellido","nombre","numero_legajo"]
