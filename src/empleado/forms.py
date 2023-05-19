""" from django import forms

class EmpleadoForm(forms.Form):
    nombre = forms.CharField(max_length= 30 , label= "Nombre")
    apellido = forms.CharField(max_length= 30 , label= " Apellido")
    numero_legajo = forms.IntegerField(min_value=0 , error_messages= "El numero de legajo no puede ser negativo ")
    activo = forms.BooleanField(label= 'Activo') """

from django.forms import ModelForm
from .models import Empleado

class EmpleadoForm(ModelForm):
		class Meta:
				model = Empleado
				fields = '__all__'
