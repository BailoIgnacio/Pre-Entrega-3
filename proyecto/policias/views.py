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
    consulta = request.GET.get("q")
    if consulta:
        policias = Policia.objects.filter(nombre__icontains=consulta)
    else:
        policias = Policia.objects.all()
    return render(request, 'policias/policia_listar.html', {'policias': policias})

def policia_detail(request, pk:int):
    query = Policia.objects.get(id=pk)
    context = {"object": query}
    return render(request, "policias/policia_detail.html", context)

def policia_update(request, pk:int):
    query = Policia.objects.get(id=pk)
    if request.method == "GET":
        form = PoliciaForm(instance=query)

    if request.method == "POST":
        form = PoliciaForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect("policias:policia_listar")
    return render(request, "policias/policia_update.html", {"form": form})

def prolicia_confirm_delete(request, pk:int):
    query = Policia.objects.get(id=pk)
    if request.method == "POST":
        query.delete()
        return redirect("policias:policia_listar")
    return render(request,"policias/policia_confirm_delete.html")