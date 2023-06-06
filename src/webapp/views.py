from django.shortcuts import render

def cargar_index(request):
    return render(request, 'home.html')