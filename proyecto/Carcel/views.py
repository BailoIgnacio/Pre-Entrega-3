from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Presos, Policia, Prision
from .forms import PrisionForm, PresosForm

def index(request):
    return render(request, "Carcel/index.html")

@login_required
def presos_list(request):
    lista_presos = Presos.objects.all()
    contexto = {"presos" : lista_presos}
    return render(request, "Carcel/presos_list.html", contexto)

def preso(request):
    return render(request, "Carcel/preso.html")

def prision(request):
    return render(request, "Carcel/prision.html")

def prision_create(request):
    if request.method == "GET":
        form = PrisionForm()

    if request.method == "POST":
        form = PrisionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("presos:prision_list")
        
    return render(request, "Carcel/prision_create.html", {"form": form})

def prision_list(request):
    consulta = request.GET.get("q")
    if consulta:
        prisiones = Prision.objects.filter(nombre__icontains=consulta)
    else:
        prisiones = Prision.objects.all()
    contexto = {"prisiones": prisiones}
    return render(request, "Carcel/prision_list.html", contexto)

def presos_create(request):
    if request.method == "GET":
        formulario = PresosForm()
        contexto = {"formulario": formulario}

    if request.method == "POST":
        formulario = PresosForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("presos:presos_list")
    return render(request,"Carcel/presos_create.html", contexto)

def presos_list(request):
    consulta = request.GET.get("q")
    if consulta:
        presos = Presos.objects.filter(nombre__icontains=consulta)
    else:
        presos = Presos.objects.all()
    contexto = {"presos": presos}
    return render(request, "Carcel/presos_list.html", contexto)

def presos_detail(request, pk: int):
    query = Presos.objects.get(id=pk)
    context = {"object": query}
    return render(request, "Carcel/presos_detail.html", context)

def prision_detail(request, pk: int):
    query = Prision.objects.get(id=pk)
    context = {"object": query}
    return render(request, "Carcel/prision_detail.html", context)

def presos_update(request, pk:int):
    query = Presos.objects.get(id=pk)
    if request.method == "GET":
        form = PresosForm(instance=query)

    if request.method == "POST":
        form = PresosForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect("presos:presos_list")
    return render(request, "Carcel/presos_update.html", {"form": form})

def prision_update(request, pk:int):
    query = Prision.objects.get(id=pk)
    if request.method == "GET":
        form = PrisionForm(instance=query)

    if request.method == "POST":
        form = PrisionForm(request.POST, instance=query)
        if form.is_valid():
            form.save()
            return redirect("presos:prision_list")
    return render(request, "Carcel/prision_update.html", {"form": form})


def presos_confirm_delete(request, pk:int):
    query = Presos.objects.get(id=pk)
    if request.method == "POST":
        query.delete()
        return redirect("presos:presos_list")
    return render(request, "Carcel/presos_confirm_delete.html", {"object": query})

def prision_confirm_delete(request, pk:int):
    query = Prision.objects.get(id=pk)
    if request.method == "POST":
        query.delete()
        return redirect("presos:prision_list")
    return render(request,"Carcel/prision_confirm_delete.html")