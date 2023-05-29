from django import forms
from .models import Empleado
from .validators import nombreValidator
class EmpleadoForm(forms.ModelForm):
		nombre  = forms.CharField(min_length=3,max_length=50, validators=[nombreValidator])
		apellido = forms.CharField(min_length=3,max_length=50, validators=[nombreValidator])
		class Meta:
				model = Empleado
				fields = ["apellido","nombre","numero_legajo"]
