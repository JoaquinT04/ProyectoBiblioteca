from django.forms import ModelForm
from .models import Libro, Autor
from .validators import isbnValidator
from django import forms


class LibroForm(ModelForm):
		autor = forms.ModelChoiceField(queryset=Autor.objects.filter(activo=True))
		isbn = forms.IntegerField(validators=[isbnValidator], widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'Ingrese el ISBN'}))
		class Meta:
				model = Libro
				fields = ["titulo","descripcion","isbn","autor"]
				widgets = {
					'titulo' : forms.TextInput(attrs={'class':'form-control','placeholder':'Ingrese el titulo'}),
					'descripcion' : forms.Textarea(attrs={'class':'form-control','placeholder':'Ingrese una descripcion','rows':3}),
				}