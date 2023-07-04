from django.forms import ModelForm
from .models import PrestamoLibro, Libro, Socio, Empleado
from django import forms

class PrestamoLibroForm(ModelForm):
	libro = forms.ModelChoiceField(queryset = Libro.objects.filter(activo = True),widget=forms.Select(attrs={'class':'form-control'}))
	socio = forms.ModelChoiceField(queryset = Socio.objects.filter(activo = True),widget=forms.Select(attrs={'class':'form-control'}))
	empleado = forms.ModelChoiceField(queryset = Empleado.objects.filter(activo = True),widget=forms.Select(attrs={'class':'form-control'}))
	class Meta():
		model = PrestamoLibro
		fields =["libro","socio","empleado"]