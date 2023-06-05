from django.forms import ModelForm
from .models import PrestamoLibro, Libro, Socio, Empleado
from django import forms
from .validators import validar_libro_disponible

class PrestamoLibroForm(ModelForm):
	libro = forms.ModelChoiceField(queryset = Libro.objects.filter(activo = True),validators=[validar_libro_disponible])
	socio = forms.ModelChoiceField(queryset = Socio.objects.filter(activo = True))
	empleado = forms.ModelChoiceField(queryset = Empleado.objects.filter(activo = True))
	class Meta():
		model = PrestamoLibro
		fields =["libro","socio","empleado"]