from django.forms import ModelForm
from .models import Empleado

class EmpleadoForm(ModelForm):
		nombre  = forms.CharField(min_length=3,max_length=50, validators=[nombreValidator])
		apellido = forms.CharField(min_length=3,max_length=50, validators=[nombreValidator])
		class Meta:
				model = Empleado
				fields = ["nombre","apellido","numero_legajo"]
