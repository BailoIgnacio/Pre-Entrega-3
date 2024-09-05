from django.urls import path, include
from . import views

app_name = "policias"

urlpatterns = [
    path("", views.index, name="index"),
    path("policia/create", views.policia_create, name="policia_create"),
    path('policia/listar', views.mostrar_policias, name='policia_listar'),
]
