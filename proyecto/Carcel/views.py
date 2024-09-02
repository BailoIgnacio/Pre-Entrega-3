from django.shortcuts import render
from .models import Presos, Policia

def index(request):
    return render(request, "Carcel/index.html")


def presos_list(request):
    lista_presos = Presos.objects.all()
    contexto = {"presos" : lista_presos}
    return render(request, "Carcel/presos_list.html", contexto)

def agregar_preso(request):
    return render(request, "Carcel/preso.html")