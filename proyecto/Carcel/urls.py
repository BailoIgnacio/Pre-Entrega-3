
from django.urls import path
from . import views

app_name = "presos"

urlpatterns = [
    path("presos/list", views.presos_list, name="agregar_preso"),
    path("", views.index, name="index")
]
