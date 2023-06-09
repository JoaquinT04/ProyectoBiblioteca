from django.forms import ModelForm
from .models import PrestamoLibro, Libro, Socio, Empleado
from django import forms
from django.utils import timezone
from datetime import timedelta

class PrestamoLibroForm(ModelForm):
	libro = forms.ModelChoiceField(queryset = Libro.objects.filter(activo = True))
	socio = forms.ModelChoiceField(queryset = Socio.objects.filter(activo = True))
	empleado = forms.ModelChoiceField(queryset = Empleado.objects.filter(activo = True))
	class Meta():
		model = PrestamoLibro
		fields =["libro","socio","empleado","fecha_devolucion"]