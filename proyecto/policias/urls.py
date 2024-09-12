from django.urls import path, include
from . import views

app_name = "policias"

urlpatterns = [
    path("", views.index, name="index"),
    path("policia/create", views.policia_create, name="policia_create"),
    path('policia/listar', views.mostrar_policias, name='policia_listar'),
    path("policia/detail/<int:pk>", views.policia_detail, name="policia_detail"),
    path("policia/update/<int:pk>", views.policia_update, name="policia_update"),
    path("policia/confirm/delete/<int:pk>", views.prolicia_confirm_delete, name="policia_confirm_delete")
]
