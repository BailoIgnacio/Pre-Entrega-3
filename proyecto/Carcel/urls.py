
from django.urls import path
from . import views

app_name = "presos"

urlpatterns = [
    path("", views.index, name="index"),
    path("presos/",views.preso, name="preso"),
    path("presos/list", views.presos_list, name="agregar_preso"),
    path("prision",views.prision, name="prision"),
    path("prision/create", views.prision_create, name="prision_create" ),
    path("prision/list", views.prision_list, name="prision_list"),
    path("presos/create", views.presos_create, name="presos_create"),
    path("presos/list", views.presos_list, name="presos_list"),
    path("presos/detail/<int:pk>", views.presos_detail, name="presos_detail"),
]
