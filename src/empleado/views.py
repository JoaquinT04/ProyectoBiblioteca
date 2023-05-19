from django.shortcuts import render
from django.views.generic import CreateView
from .models import Empleado
# Create your views here.

class CategoryCreateView(CreateView()):
	model = Empleado