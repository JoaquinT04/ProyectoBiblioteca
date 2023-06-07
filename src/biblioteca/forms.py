from django.forms import ModelForm
from .models import PrestamoLibro, Libro, Socio, Empleado
from django import forms
from .validators import validar_libro_disponible
from django.utils import timezone
from datetime import timedelta

class PrestamoLibroForm(ModelForm):
	fecha_prestamos = forms.DateTimeField(disabled=False, initial=timezone.now)
	fecha_devolucion = forms.DateTimeField(disabled=False, initial=timezone.now() + timedelta(days=2))
	libro = forms.ModelChoiceField(queryset = Libro.objects.filter(activo = True),validators=[validar_libro_disponible])
	socio = forms.ModelChoiceField(queryset = Socio.objects.filter(activo = True))
	empleado = forms.ModelChoiceField(queryset = Empleado.objects.filter(activo = True))
	class Meta():
		model = PrestamoLibro
		fields =["libro","socio","empleado","fecha_prestamos","fecha_devolucion"]