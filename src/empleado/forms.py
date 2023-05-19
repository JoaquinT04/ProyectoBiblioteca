from django import forms

class EmpleadoForm(forms.Form):
    nombre = forms.CharField(max_length=50, label="Nombre")
    apellido= forms.CharField(max_length=50, label="Apellido")
    numero_legajo = forms.IntegerField(max_length=30,label="Nro de legajo")
