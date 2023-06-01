from django.forms import ModelForm
from .models import PrestamoLibro
from .models import Libro
from .models import Socio
from .models import Empleado
from django import forms
from .validators import nombreValidator

class PrestamoLibroForm(ModelForm):
	libro = forms.ModelChoiceField(queryset = Libro.objects.filter(activo = True))
	socio = forms.ModelChoiceField(queryset = Socio.objects.filter(activo = True))
	empleado = forms.ModelChoiceField(queryset = Empleado.objects.filter(activo = True))
	class Meta():
		model = PrestamoLibro
		fields =["fecha_prestamos","fecha_devolucion","libro","socio","empleado"]