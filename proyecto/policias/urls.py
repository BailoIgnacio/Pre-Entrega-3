from django.urls import path, include
from . import views
from django.contrib.auth.decorators import login_required

app_name = "policias"

urlpatterns = [
    path("", login_required(views.index), name="index"),
    path("policia/create", login_required(views.policia_create), name="policia_create"),
    path('policia/listar', login_required(views.mostrar_policias), name='policia_listar'),
    path("policia/detail/<int:pk>", login_required(views.policia_detail), name="policia_detail"),
    path("policia/update/<int:pk>", login_required(views.policia_update), name="policia_update"),
    path("policia/confirm/delete/<int:pk>", login_required(views.prolicia_confirm_delete), name="policia_confirm_delete")
]