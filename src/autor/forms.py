from django.forms import ModelForm
from .models import Autor

class AutorForm(ModelForm):
		class Meta:
				model = Autor
				fields = '__all__'
