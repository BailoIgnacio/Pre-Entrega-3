from django.shortcuts import render, redirect
from .forms import PoliciaForm
from .models import Policia

def index(request):
    return render(request, "policias/index.html")

def policia_create(request):
    if request.method == "GET":
        formulario = PoliciaForm()
        contexto = {"formulario": formulario}

    if request.method == "POST":
        formulario = PoliciaForm(request.POST)
        contexto = {"formulario": formulario}
        if formulario.is_valid():
            formulario.save()
            return redirect("policias:policia_listar")
    return render(request, "policias/policia_create.html", contexto)

def mostrar_policias(request):
    policias = Policia.objects.all()
    return render(request, 'policias/policia_listar.html', {'policias': policias})
