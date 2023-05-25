from django.shortcuts import get_object_or_404 , redirect
from .models import Empleado
from .forms import EmpleadoForm
from django.views.generic import UpdateView, ListView,CreateView
from django.urls import reverse_lazy

class EditarEmpleado(UpdateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = 'empleados/editar.html' 
    success_url = reverse_lazy('empleados:ListarEmpleados')  

class ListarEmpleados(ListView):
    model = Empleado
    template_name = "empleados/listar.html"
    ordering = 'pk'
        
class CrearEmpleado(CreateView):
    model = Empleado
    form_class = EmpleadoForm
    template_name = "empleados/crear.html"
    success_url = reverse_lazy('empleados:ListarEmpleados') 

# Create your views here.
def activar_empleado(request, id):
    empleado= get_object_or_404(Empleado, id = id)
    empleado.activo = True
    empleado.save()
    
    return redirect(reverse_lazy('empleados:ListarEmpleados'))

def desactivar_empleado(request, id):
    empleado = get_object_or_404(Empleado, id=id)
    empleado.activo = False
    empleado.save()

    return redirect(reverse_lazy('empleados:ListarEmpleados'))

